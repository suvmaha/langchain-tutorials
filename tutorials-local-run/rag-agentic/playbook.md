# Playbook — Agentic RAG

**Estimated time:** ~15 min (clone ~1 min + install ~3 min + run ~5 min)

An agent that retrieves context from a blog post to answer questions. The agent decides when to retrieve, what to query, and retrieves multiple times per question when needed. Default: Claude Opus via Anthropic API. Zero-cost alternative: Ollama (see STEP 6).

---

## Table of Contents

- [STEP 0 — Clone the Repo](#step-0--clone-the-repo)
- [STEP 1 — Create Virtual Environment](#step-1--create-virtual-environment)
- [STEP 2 — Verify Tools](#step-2--verify-tools)
- [STEP 3 — Set API Key](#step-3--set-api-key)
- [STEP 4 — Install Python Dependencies](#step-4--install-python-dependencies)
- [STEP 5 — Run the Agent](#step-5--run-the-agent)
- [STEP 6 — Run with Ollama (Zero API Cost)](#step-6--run-with-ollama-zero-api-cost)
- [STEP 7 — Switch Models](#step-7--switch-models)

---

## STEP 0 — Clone the Repo

```bash
git clone https://github.com/suvmaha/langchain-tutorials.git
cd langchain-tutorials

# Set REPO_ROOT — all paths in this playbook are relative to here
export REPO_ROOT=$(pwd)
```

---

## STEP 1 — Create Virtual Environment

```bash
cd $REPO_ROOT/tutorials-local-run/rag-agentic

python3 -m venv .venv
source .venv/bin/activate

# Verify
which python   # should point to .venv/bin/python
```

---

## STEP 2 — Verify Tools

```bash
python --version    # 3.11+
```

---

## STEP 3 — Set API Key

```bash
export ANTHROPIC_API_KEY=<your-key>
```

---

## STEP 4 — Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

## STEP 5 — Run the Agent

```bash
python agent.py

# OUTPUT
# LLM        : anthropic/claude-opus-4-7
# Embeddings : huggingface/all-MiniLM-L6-v2
#
# Loading document...
#   43,047 characters loaded
# Splitting into chunks...
#   63 chunks
# Embedding and indexing...
#   Done
#
# Q: What is Task Decomposition?
# ------------------------------------------------------------
#   [Tool] retrieve_context(query='Task Decomposition')
# A: Task Decomposition is a planning technique used by LLM-powered agents
#    to break down complicated, multi-step tasks into smaller, simpler,
#    more manageable subtasks...
#    Key approaches: Chain of Thought (CoT), Tree of Thoughts (ToT), LLM+P
#
# Q: What is the standard method for Task Decomposition? Once you get the
#    answer, look up common extensions of that method.
# ------------------------------------------------------------
#   [Tool] retrieve_context(query='standard method for task decomposition')
#   [Tool] retrieve_context(query='Chain of Thought extensions Tree of Thoughts')
# A: The standard method is Chain of Thought (CoT) (Wei et al. 2022)...
#    Common extensions: Tree of Thoughts (ToT) adds branching + search;
#    LLM+P combines LLM reasoning with classical planning tools (PDDL)...
```

> The second question triggers **three retrieval calls** — Claude retrieved once for the standard method (CoT), then twice more for extensions (ToT, ReAct, LLM+P). That's the agentic behavior: the agent decides to keep retrieving until it has enough information.

---

## STEP 6 — Run with Ollama (Zero API Cost)

> This is an alternative to STEP 5 — skip it if you're using Claude. Ollama runs entirely locally with no API key and no cost, but smaller models (llama3.2, 3B) do not reliably perform multi-step tool calling. Use this path to explore the zero-cost option, not for the full agentic demo.

No API key needed. Requires Ollama installed and models pulled.

```bash
# Pull models (one-time, ~2.3 GB total)
ollama pull llama3.2
ollama pull nomic-embed-text

# Install Ollama dep
pip install langchain-ollama

export MODEL_PRESET=ollama-full
python agent.py

# LLM        : ollama/llama3.2
# Embeddings : ollama/nomic-embed-text
```

> Note: `llama3.2` (3B) handles single-step retrieval correctly but does not reliably perform multi-step tool calling. Q1 will retrieve from the blog; Q2 will make one call and may not identify CoT as the standard method.

Install Ollama if missing: https://ollama.com/download

---

## STEP 7 — Switch Models

**Use a different Anthropic model:**

```bash
export MODEL_PRESET=anthropic
export LLM_MODEL=claude-sonnet-4-6

python agent.py

# LLM        : anthropic/claude-sonnet-4-6
```

**Use a different Ollama model:**

```bash
export MODEL_PRESET=ollama-full
export LLM_MODEL=llama3.1

python agent.py

# LLM        : ollama/llama3.1
```

> Always run `unset LLM_MODEL` before switching presets, otherwise the model name from one provider will be sent to the other.

---

## How It Works

```
agent.py
├── load_and_index()          — fetch blog post, chunk, embed, store in memory
├── make_retriever_tool()     — wrap vector store as a @tool the agent can call
├── make_agent()              — create_agent(model, tools, system_prompt)
└── run_query()               — stream agent responses, print tool calls + answer

config.py
└── get_model_config()        — reads MODEL_PRESET env var, returns provider/model names
```

The agent loop:
```
User question
    ↓
Agent decides: call retrieve_context(query)?
    ↓ yes — retrieves top-4 chunks
Agent reads chunks, decides: enough information?
    ↓ no  — calls retrieve_context again with a different query
    ↓ yes — generates final answer
```

---

## Cleanup

```bash
# Deactivate the virtual environment
deactivate

# Remove the venv to free disk space (~1 GB)
rm -rf .venv

# Unset any env vars if you changed the model
unset MODEL_PRESET
unset LLM_MODEL
unset EMBEDDINGS_MODEL
unset ANTHROPIC_API_KEY
```

---

## Common Issues

**`ollama: command not found`:**
Install from https://ollama.com/download and restart your terminal.

**`model not found` error (Ollama):**
Run `ollama pull llama3.2` and `ollama pull nomic-embed-text` first.

**`.venv not activated`:**
Run `source .venv/bin/activate` — your prompt should show `(.venv)`.

**`ImportError: langchain_anthropic`:**
Run `pip install -r requirements.txt` with the venv activated.

**`NotFoundError: model: llama3.1` (or other Ollama model name on Anthropic):**
You have `LLM_MODEL` set from a previous run. Run `unset LLM_MODEL` before switching presets.
