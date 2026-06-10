# Playbook — Agentic RAG

**Estimated time:** ~20 min (clone ~1 min + model pull ~5 min + install ~3 min + run ~10 min)

An agent that retrieves context from a blog post to answer questions. The agent decides when to retrieve, what to query, and can retrieve multiple times per question. Runs locally with Ollama — zero API cost. Use the Anthropic preset to see the full multi-retrieval agentic behavior.

---

## Table of Contents

- [STEP 0 — Clone the Repo](#step-0--clone-the-repo)
- [STEP 1 — Create Virtual Environment](#step-1--create-virtual-environment)
- [STEP 2 — Verify Tools](#step-2--verify-tools)
- [STEP 3 — Pull Ollama Models](#step-3--pull-ollama-models)
- [STEP 4 — Install Python Dependencies](#step-4--install-python-dependencies)
- [STEP 5 — Run the Agent (Ollama)](#step-5--run-the-agent-ollama)
- [STEP 6 — Run with Claude (Full Agentic Demo)](#step-6--run-with-claude-full-agentic-demo)
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
ollama --version    # any recent version
```

Install Ollama if missing: https://ollama.com/download

---

## STEP 3 — Pull Ollama Models

```bash
# LLM
ollama pull llama3.2

# Embeddings
ollama pull nomic-embed-text

# Verify
ollama list

# OUTPUT
# NAME                       ID              SIZE      MODIFIED
# nomic-embed-text:latest    0a109f422b47    274 MB    ...
# llama3.2:latest            a80c4f17acd5    2.0 GB    ...
```

---

## STEP 4 — Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

## STEP 5 — Run the Agent (Ollama)

```bash
python agent.py

# OUTPUT
# LLM        : ollama/llama3.2
# Embeddings : ollama/nomic-embed-text
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
# A: Task Decomposition is the process of breaking down a complex task or
#    problem into smaller, more manageable sub-tasks or steps...
#
# Q: What is the standard method for Task Decomposition? Once you get the
#    answer, look up common extensions of that method.
# ------------------------------------------------------------
#   [Tool] retrieve_context(query='Task Decomposition methods')
# A: ...
```

> With `llama3.2`, Q1 retrieves correctly from the blog. Q2 makes a single tool call — local 3B models don't reliably perform multi-step tool calling. See STEP 6 for the full agentic demo with Claude.

---

## STEP 6 — Run with Claude (Full Agentic Demo)

```bash
pip install langchain-anthropic langchain-huggingface sentence-transformers

export ANTHROPIC_API_KEY=<your-key>
export MODEL_PRESET=anthropic
unset LLM_MODEL   # clear any model override from previous runs

python agent.py

# OUTPUT
# LLM        : anthropic/claude-haiku-4-5-20251001
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
# A: Based on the blog post about LLM-powered agents, Task Decomposition is
#    the process of breaking down complex tasks into smaller, more manageable
#    steps. Task decomposition can be done by LLM with simple prompting,
#    using task-specific instructions, or with human inputs...
#
# Q: What is the standard method for Task Decomposition? Once you get the
#    answer, look up common extensions of that method.
# ------------------------------------------------------------
#   [Tool] retrieve_context(query='Task Decomposition standard method')
#   [Tool] retrieve_context(query='Chain of Thought extensions improvements')
#   [Tool] retrieve_context(query='Tree of Thoughts method')
# A: The standard method for Task Decomposition is Chain of Thought (CoT)
#    prompting (Wei et al. 2022)...
#    Common extensions include Tree of Thoughts (ToT), ReAct, and LLM+P...
```

> The second question triggers **three retrieval calls** — Claude retrieved once for the standard method (CoT), then twice more for extensions (ToT, ReAct, LLM+P). That's the agentic behavior: the agent decides to keep retrieving until it has enough information.

---

## STEP 7 — Switch Models

**Use a different Ollama model:**

```bash
ollama pull llama3.1

export LLM_MODEL=llama3.1
python agent.py

# LLM        : ollama/llama3.1
```

**Use Claude Sonnet instead of Haiku:**

```bash
export MODEL_PRESET=anthropic
export LLM_MODEL=claude-sonnet-4-6

python agent.py

# LLM        : anthropic/claude-sonnet-4-6
```

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

## Common Issues

**`ollama: command not found`:**
Install from https://ollama.com/download and restart your terminal.

**`model not found` error:**
Run `ollama pull llama3.2` and `ollama pull nomic-embed-text` first.

**`.venv not activated`:**
Run `source .venv/bin/activate` — your prompt should show `(.venv)`.

**`ImportError: langchain_anthropic`:**
Run `pip install langchain-anthropic langchain-huggingface sentence-transformers` before switching to `MODEL_PRESET=anthropic`.

**`NotFoundError: model: llama3.1` (or other Ollama model name):**
You have `LLM_MODEL` set from a previous run. Run `unset LLM_MODEL` before switching presets.
