# Playbook — Agentic RAG

**Estimated time:** ~10 min (model pull ~3 min + install ~2 min + run ~5 min)

An agent that retrieves context from a blog post to answer questions. The agent decides when to retrieve, what to query, and can retrieve multiple times per question. Runs locally with Ollama — zero API cost.

---

## Table of Contents

- [STEP 0 — Clone the Repo](#step-0--clone-the-repo)
- [STEP 1 — Verify Tools](#step-1--verify-tools)
- [STEP 2 — Pull Ollama Models](#step-2--pull-ollama-models)
- [STEP 3 — Install Python Dependencies](#step-3--install-python-dependencies)
- [STEP 4 — Run the Agent](#step-4--run-the-agent)
- [STEP 5 — Switch Models](#step-5--switch-models)

---

## STEP 0 — Clone the Repo

```bash
git clone https://github.com/suvmaha/langchain-tutorials.git
cd langchain-tutorials

# Set REPO_ROOT — all paths in this playbook are relative to here
export REPO_ROOT=$(pwd)
```

---

## STEP 1 — Verify Tools

```bash
python --version    # 3.11+
ollama --version    # any recent version
```

Install Ollama if missing: https://ollama.com/download

---

## STEP 2 — Pull Ollama Models

```bash
# LLM
ollama pull llama3.2

# Embeddings
ollama pull nomic-embed-text

# Verify
ollama list

# OUTPUT (example)
# NAME                    ID              SIZE
# llama3.2:latest         ...             2.0 GB
# nomic-embed-text:latest ...             274 MB
```

---

## STEP 3 — Install Python Dependencies

```bash
cd $REPO_ROOT/tutorials-local-run/rag-agentic

pip install -r requirements.txt
```

---

## STEP 4 — Run the Agent

```bash
python agent.py

# OUTPUT
LLM        : ollama/llama3.2
Embeddings : ollama/nomic-embed-text

Loading document...
  43,131 characters loaded
Splitting into chunks...
  66 chunks
Embedding and indexing...
  Done

Q: What is Task Decomposition?
------------------------------------------------------------
  [Tool] retrieve_context(query='Task Decomposition')
A: Task Decomposition is a technique used to break down complex tasks into
   smaller, more manageable steps...

Q: What is the standard method for Task Decomposition? Once you get the
   answer, look up common extensions of that method.
------------------------------------------------------------
  [Tool] retrieve_context(query='standard method for Task Decomposition')
  [Tool] retrieve_context(query='common extensions of Chain of Thought')
A: The standard method for Task Decomposition is Chain of Thought (CoT)...
   Common extensions include...
```

> The second question triggers **two retrieval calls** — the agent retrieved once for the standard method, then again for the extensions. That's the agentic behavior: the agent decides to make a second call rather than stopping after the first.

---

## STEP 5 — Switch Models

**Use Claude (Anthropic):**

```bash
pip install langchain-anthropic langchain-huggingface sentence-transformers

export ANTHROPIC_API_KEY=<your-key>
export MODEL_PRESET=anthropic

python agent.py

# LLM        : anthropic/claude-haiku-4-5-20251001
# Embeddings : huggingface/all-MiniLM-L6-v2
```

**Use a different Ollama model:**

```bash
ollama pull mistral

export LLM_MODEL=mistral
python agent.py

# LLM        : ollama/mistral
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
    ↓ yes — retrieves top-2 chunks
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

**Slow first run:**
HuggingFace embeddings download the model on first use (~90 MB). Subsequent runs use the cache.

**`ImportError: langchain_anthropic`:**
Run `pip install langchain-anthropic` before switching to `MODEL_PRESET=anthropic`.
