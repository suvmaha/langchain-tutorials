# Playbook — RAG 2-Step (Retrieve then Generate)

**Estimated time:** ~10 min (clone ~1 min + install ~3 min + run ~5 min)

Simple, predictable RAG. Retrieval always happens first — the LLM never decides whether or when to retrieve. Step 1 retrieves the top-k relevant chunks. Step 2 passes them to the LLM to generate an answer. Compare to [rag-agentic](../rag-agentic/) where the agent decides when and what to retrieve.

---

## Table of Contents

- [STEP 0 — Clone the Repo](#step-0--clone-the-repo)
- [STEP 1 — Create Virtual Environment](#step-1--create-virtual-environment)
- [STEP 2 — Verify Tools](#step-2--verify-tools)
- [STEP 3 — Set API Key](#step-3--set-api-key)
- [STEP 4 — Install Python Dependencies](#step-4--install-python-dependencies)
- [STEP 5 — Run the Chain](#step-5--run-the-chain)
- [STEP 6 — Switch Models](#step-6--switch-models)

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
cd $REPO_ROOT/tutorials-local-run/rag-2step

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

## STEP 5 — Run the Chain

```bash
python chain.py

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
#   [Step 1 — Retrieved 4 chunks]
#     1. Task decomposition can be done (1) by LLM with simple prompting like "Steps for XYZ.\n1."...
#     2. Component One: Planning# A complicated task usually involves many steps. An agent needs...
#     3. Finite context length: The restricted context capacity limits the inclusion of historical...
#     4. Illustration of how HuggingGPT works...
#
# A: Task decomposition is a technique used to break down complex tasks into smaller and simpler
#    steps. It involves transforming big tasks into multiple manageable tasks...
#
# Q: What are the main types of memory in LLM agents?
# ------------------------------------------------------------
#   [Step 1 — Retrieved 4 chunks]
#     1. Memory  Short-term memory: I would consider all the in-context learning...
#     2. Memory stream: is a long-term memory module (external database)...
#     3. Comparison of AD, ED, source policy and RL^2 on environments...
#     4. LLM Powered Autonomous Agents  Date: June 23, 2023...
#
# A: The main types of memory in LLM agents are:
#    1. Short-term memory — in-context learning within the current context window
#    2. Long-term memory — external vector store for retaining information over time
```

> Notice: **Step 1 always runs** before Step 2, regardless of the question. The LLM never decides whether to retrieve — it always gets context first. This predictability is the trade-off vs Agentic RAG.

---

## STEP 6 — Switch Models

**Use a different Anthropic model:**

```bash
export LLM_MODEL=claude-sonnet-4-6
python chain.py

# LLM        : anthropic/claude-sonnet-4-6
```

**Use Ollama (zero API cost):**

```bash
pip install langchain-ollama
ollama pull llama3.2
ollama pull nomic-embed-text

export MODEL_PRESET=ollama-full
unset LLM_MODEL
python chain.py

# LLM        : ollama/llama3.2
```

> Unlike rag-agentic, the 2-step pattern works well with smaller models — retrieval is handled by the code, not the model. llama3.2 will answer correctly as long as the retrieved chunks contain the answer.

---

## How It Works

```
chain.py
├── load_and_index()        — fetch blog post, chunk, embed, store in memory
├── make_chain()            — build retriever + prompt | model | parser chain
└── run_query()             — Step 1: retrieve chunks, Step 2: generate answer

config.py
└── get_model_config()      — reads MODEL_PRESET env var, returns provider/model names
```

The chain:
```
User question
    ↓
Step 1: retriever.invoke(question)  — vector similarity search, returns top-4 chunks
    ↓
Step 2: gen_chain.invoke({context, question})  — LLM reads chunks, generates answer
    ↓
Answer
```

---

## Agentic RAG vs 2-Step RAG

| | 2-Step RAG | Agentic RAG |
|---|---|---|
| Retrieval | Always, once | Agent decides if/when/how many times |
| Control | You control it | LLM controls it |
| Predictability | High | Lower |
| Multi-step reasoning | No | Yes |
| Model requirement | Any | Capable tool-calling model |
| Best for | Known retrieval need | Complex, open-ended questions |

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

**`.venv not activated`:**
Run `source .venv/bin/activate` — your prompt should show `(.venv)`.

**`ImportError: langchain_anthropic`:**
Run `pip install -r requirements.txt` with the venv activated.

**`NotFoundError: model: llama3.2` on Anthropic:**
You have `LLM_MODEL` set from a previous run. Run `unset LLM_MODEL` before switching presets.
