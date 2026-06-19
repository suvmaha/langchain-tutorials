# LangChain Tutorials

Hands-on tutorials for LangChain and LangGraph — agents, evaluations, and CI/CD pipelines. Each tutorial includes a step-by-step playbook for 100% repeatable execution.

## Certified

Tutorials run end-to-end and confirmed working:

| Tutorial | Date | Model / Environment |
|----------|------|---------------------|
| [rag-semantic-search](tutorials-local-run/rag-semantic-search/) | 2026-06-11 | huggingface/all-MiniLM-L6-v2 |
| [rag-2step](tutorials-local-run/rag-2step/) | 2026-06-11 | anthropic/claude-opus-4-7 |
| [rag-agentic](tutorials-local-run/rag-agentic/) | 2026-06-11 | anthropic/claude-opus-4-7 |

---

## Tutorials

| Tutorial | What It Covers | Status |
|----------|---------------|--------|
| [evals-cicd-basic](tutorials/evals-cicd-basic/) | Multi-agent evaluation in CI/CD — the minimal viable pattern | planned |
| [cicd-pipeline](tutorials/cicd-pipeline/) | Full code-to-production pipeline with LLM quality gates | planned |
| [offline-evals](tutorials/offline-evals/) | Production-grade evals: trajectory matching, tool validation, daily cron, Slack | planned |
| [evals-playwright](tutorials/evals-playwright/) | Browser-based UI evaluation with Playwright | planned |

## Study Order

Start with `evals-cicd-basic` — it explains why LLM evaluation belongs in CI/CD with minimal noise. Then `cicd-pipeline` adds deployment and completes the code-to-production story. Then `offline-evals` for production depth.

## Local-Run Tutorials

No cluster or cloud needed — just Python and an API key.

| Tutorial | Framework | What It Covers | Status |
|----------|-----------|---------------|--------|
| [rag-semantic-search](tutorials-local-run/rag-semantic-search/) | LangChain | Semantic search — embeddings + vector store foundation | ✅ Certified |
| [rag-2step](tutorials-local-run/rag-2step/) | LangChain | Retrieve then generate — simple, predictable RAG | ✅ Certified |
| [rag-agentic](tutorials-local-run/rag-agentic/) | LangGraph | Agent decides when and what to retrieve | ✅ Certified |
| [sql-agent](tutorials-local-run/sql-agent/) | LangChain | SQL agent with human-in-the-loop | planned |
| [voice-agent](tutorials-local-run/voice-agent/) | LangChain | Speak to and listen to an agent | planned |
| [custom-sql-agent](tutorials-local-run/custom-sql-agent/) | LangGraph | SQL agent with full graph control | planned |
| [personal-assistant](tutorials-local-run/personal-assistant/) | LangGraph | Supervisor delegating to subagents | planned |
| [customer-support](tutorials-local-run/customer-support/) | LangGraph | Agent state transitions and handoffs | planned |
| [knowledge-base-router](tutorials-local-run/knowledge-base-router/) | LangGraph | Query routing to specialized agents | planned |
| [sql-assistant-skills](tutorials-local-run/sql-assistant-skills/) | LangGraph | Progressive skill loading | planned |
| [data-analysis](tutorials-local-run/data-analysis/) | Deep Agents | Data analysis with Slack reporting | planned |
| [deep-research](tutorials-local-run/deep-research/) | Deep Agents | Multi-step research with reflection | planned |

## Source Material

These tutorials are based on examples from the LangChain samples collection, extended with:
- Step-by-step playbooks for repeatability
- Additional automation where missing
- Annotations explaining the patterns and design decisions
