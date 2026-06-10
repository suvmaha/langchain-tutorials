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

## Source Material

These tutorials are based on examples from the LangChain samples collection, extended with:
- Step-by-step playbooks for repeatability
- Additional automation where missing
- Annotations explaining the patterns and design decisions
