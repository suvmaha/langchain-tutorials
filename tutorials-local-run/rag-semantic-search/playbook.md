# Playbook — RAG Semantic Search

**Estimated time:** ~8 min (clone ~1 min + install ~3 min + run ~3 min)

The foundation layer of RAG — no LLM, no generation. Embeds a document into a vector store and searches it by semantic similarity. Returns scored chunks showing which parts of the document are most relevant to each query. Compare to [rag-2step](../rag-2step/) which adds LLM generation on top, and [rag-agentic](../rag-agentic/) which adds an agent loop.

**No API key needed** — uses HuggingFace embeddings locally by default.

---

## Table of Contents

- [STEP 0 — Clone the Repo](#step-0--clone-the-repo)
- [STEP 1 — Create Virtual Environment](#step-1--create-virtual-environment)
- [STEP 2 — Verify Tools](#step-2--verify-tools)
- [STEP 3 — Install Python Dependencies](#step-3--install-python-dependencies)
- [STEP 4 — Run the Search](#step-4--run-the-search)
- [STEP 5 — Switch Embeddings](#step-5--switch-embeddings)

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
cd $REPO_ROOT/tutorials-local-run/rag-semantic-search

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

## STEP 3 — Install Python Dependencies

```bash
pip install -r requirements.txt
```

No API key needed for this tutorial.

---

## STEP 4 — Run the Search

```bash
python search.py

# OUTPUT
# Embeddings : huggingface/all-MiniLM-L6-v2
#
# Loading document...
#   43,047 characters loaded
# Splitting into chunks...
#   63 chunks
# Embedding and indexing...
#   Done
#
# Query: What is Task Decomposition?
# ------------------------------------------------------------
#   [1] score=0.xxx  Task decomposition can be done (1) by LLM with simple prompting like...
#   [2] score=0.xxx  Component One: Planning# A complicated task usually involves many steps...
#   [3] score=0.xxx  Chain of thought (CoT; Wei et al. 2022) has become a standard prompting...
#   [4] score=0.xxx  ...
#
# Query: What are the main types of memory in LLM agents?
# ------------------------------------------------------------
#   [1] score=0.xxx  Memory  Short-term memory: I would consider all the in-context learning...
#   [2] score=0.xxx  Memory stream: is a long-term memory module (external database)...
#   [3] score=0.xxx  ...
#
# Query: How does the ReAct framework work?
# ------------------------------------------------------------
#   [1] score=0.xxx  ReAct (Yao et al. 2023) integrates reasoning and acting within LLM...
#   [2] score=0.xxx  ...
```

> The `score` is cosine similarity — higher means more relevant. Notice how different queries pull different chunks from the same document. This is what rag-2step and rag-agentic use under the hood before passing chunks to the LLM.

---

## STEP 5 — Switch Embeddings

**Use Ollama embeddings (zero API cost, local model):**

```bash
ollama pull nomic-embed-text

pip install langchain-ollama
export EMBEDDINGS_PRESET=ollama

python search.py

# Embeddings : ollama/nomic-embed-text
```

**Use OpenAI embeddings:**

```bash
pip install langchain-openai
export OPENAI_API_KEY=<your-key>
export EMBEDDINGS_PRESET=openai

python search.py

# Embeddings : openai/text-embedding-3-small
```

---

## How It Works

```
search.py
├── load_and_index()    — fetch blog post, chunk, embed, store in InMemoryVectorStore
└── run_search()        — similarity_search_with_score(query, k=4) → print scored chunks

config.py
└── get_embeddings_config()  — reads EMBEDDINGS_PRESET env var, returns provider/model
```

What happens inside `load_and_index()`:
```
Blog post HTML
    ↓
BeautifulSoup — strip to article content
    ↓
RecursiveCharacterTextSplitter — 63 chunks of ~1000 chars, 200 overlap
    ↓
HuggingFaceEmbeddings — each chunk → 384-dim vector
    ↓
InMemoryVectorStore — stores all vectors in memory
```

What happens inside `run_search()`:
```
Query string
    ↓
Embed query → 384-dim vector
    ↓
Cosine similarity against all 63 stored vectors
    ↓
Return top-4 by score
```

---

## The Three RAG Tutorials

| Tutorial | What it adds |
|----------|-------------|
| rag-semantic-search | Embed + search — returns scored chunks, no LLM |
| rag-2step | Adds LLM generation — chunks become context, LLM answers |
| rag-agentic | Adds agent loop — LLM decides when and what to retrieve |

---

## Cleanup

```bash
# Deactivate the virtual environment
deactivate

# Remove the venv to free disk space (~500 MB)
rm -rf .venv

# Unset any env vars if you changed the preset
unset EMBEDDINGS_PRESET
unset EMBEDDINGS_MODEL
```

---

## Common Issues

**`.venv not activated`:**
Run `source .venv/bin/activate` — your prompt should show `(.venv)`.

**`ImportError: sentence_transformers`:**
Run `pip install -r requirements.txt` with the venv activated.

**`ollama: command not found`:**
Install from https://ollama.com/download — only needed for `EMBEDDINGS_PRESET=ollama`.
