# LangChain Tutorials

Hands-on tutorials for LangChain and LangGraph — agents, evaluations, and CI/CD pipelines. Each tutorial includes a step-by-step playbook for 100% repeatable execution.

## Tutorials

| Tutorial | What It Covers |
|----------|---------------|
| [evals-cicd-basic](tutorials/evals-cicd-basic/) | Multi-agent evaluation in CI/CD — the minimal viable pattern |
| [cicd-pipeline](tutorials/cicd-pipeline/) | Full code-to-production pipeline with LLM quality gates |
| [offline-evals](tutorials/offline-evals/) | Production-grade evals: trajectory matching, tool validation, daily cron, Slack |
| [evals-playwright](tutorials/evals-playwright/) | Browser-based UI evaluation with Playwright |

## Study Order

Start with `evals-cicd-basic` — it explains why LLM evaluation belongs in CI/CD with minimal noise. Then `cicd-pipeline` adds deployment and completes the code-to-production story. Then `offline-evals` for production depth.

## Local-Run Tutorials

No cluster or cloud needed — just Python and an API key.

| Tutorial | Framework | What It Covers |
|----------|-----------|---------------|
| [rag-semantic-search](tutorials-local-run/rag-semantic-search/) | LangChain | Semantic search — embeddings + vector store foundation |
| [rag-2step](tutorials-local-run/rag-2step/) | LangChain | Retrieve then generate — simple, predictable RAG |
| [rag-agentic](tutorials-local-run/rag-agentic/) | LangGraph | Agent decides when and what to retrieve |
| [sql-agent](tutorials-local-run/sql-agent/) | LangChain | SQL agent with human-in-the-loop |
| [voice-agent](tutorials-local-run/voice-agent/) | LangChain | Speak to and listen to an agent |
| [custom-sql-agent](tutorials-local-run/custom-sql-agent/) | LangGraph | SQL agent with full graph control |
| [personal-assistant](tutorials-local-run/personal-assistant/) | LangGraph | Supervisor delegating to subagents |
| [customer-support](tutorials-local-run/customer-support/) | LangGraph | Agent state transitions and handoffs |
| [knowledge-base-router](tutorials-local-run/knowledge-base-router/) | LangGraph | Query routing to specialized agents |
| [sql-assistant-skills](tutorials-local-run/sql-assistant-skills/) | LangGraph | Progressive skill loading |
| [data-analysis](tutorials-local-run/data-analysis/) | Deep Agents | Data analysis with Slack reporting |
| [deep-research](tutorials-local-run/deep-research/) | Deep Agents | Multi-step research with reflection |

## Source Material

These tutorials are based on examples from the LangChain samples collection, extended with:
- Step-by-step playbooks for repeatability
- Additional automation where missing
- Annotations explaining the patterns and design decisions
