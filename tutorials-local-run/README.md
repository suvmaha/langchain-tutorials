# Local-Run Tutorials

Tutorials that run entirely on your laptop — no EKS cluster, no cloud setup required.
Just Python and an Anthropic (or OpenAI) API key.

## Prerequisites

```bash
python3 --version    # 3.10+
pip install langchain langchain-anthropic langgraph
export ANTHROPIC_API_KEY=sk-...
```

Each tutorial has its own `requirements.txt` — install from there for exact versions.

## Tutorials

| Tutorial | Framework | What It Covers | Status |
|----------|-----------|---------------|--------|
| [rag-semantic-search](rag-semantic-search/) | LangChain | Embeddings + vector store + similarity search | ✅ Certified |
| [rag-2step](rag-2step/) | LangChain | Retrieve then generate — simple, predictable RAG | ✅ Certified |
| [rag-agentic](rag-agentic/) | LangGraph | Agent decides when and what to retrieve | ✅ Certified |
| [sql-agent](sql-agent/) | LangChain | SQL agent with human-in-the-loop | planned |
| [voice-agent](voice-agent/) | LangChain | Speak to and listen to an agent | planned |
| [custom-sql-agent](custom-sql-agent/) | LangGraph | SQL agent with full graph control | planned |
| [personal-assistant](personal-assistant/) | LangGraph | Supervisor delegating to subagents | planned |
| [customer-support](customer-support/) | LangGraph | Agent state transitions and handoffs | planned |
| [knowledge-base-router](knowledge-base-router/) | LangGraph | Query routing to specialized agents | planned |
| [sql-assistant-skills](sql-assistant-skills/) | LangGraph | Progressive skill loading | planned |
| [data-analysis](data-analysis/) | Deep Agents | Data analysis with Slack reporting | planned |
| [deep-research](deep-research/) | Deep Agents | Multi-step research with reflection | planned |

## Suggested Order

**Start here if you're new to RAG:**
1. `rag-semantic-search` — understand embeddings and vector search first
2. `rag-2step` — add generation to the retrieval
3. `rag-agentic` — let the agent decide when to retrieve

**Then agents:**
4. `sql-agent` — tool use and human-in-the-loop pattern
5. `custom-sql-agent` — same problem, more control with LangGraph
6. `personal-assistant` — multi-agent with a supervisor

**Production patterns:**
7. `knowledge-base-router`, `sql-assistant-skills`, `customer-support`

## What "Certified" means

A certified tutorial has been run end-to-end in a clean environment with all output
captured and saved in its `playbook.md`. The playbook is the single source of truth —
follow it exactly and it will work.

## Source Material

These tutorials follow the official LangChain Learn page:
https://docs.langchain.com/oss/python/learn

Each folder here corresponds directly to a tutorial listed there — same structure,
extended with step-by-step playbooks, real run output, and annotations.
