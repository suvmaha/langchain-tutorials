# Evals in CI/CD — Basic

Minimal pattern for integrating LangSmith evaluations into a GitHub Actions pipeline. A multi-agent system (supervisor + invoice agent + music agent) evaluated on semantic correctness with results posted as PR comments.

## What It Covers

- Multi-agent routing with LangGraph supervisor
- LLM-as-judge evaluation (semantic correctness)
- GitHub Actions: evaluate job → report job
- Threshold-based pass/fail (70% correctness)
- PR comment reporting

## Source

Based on [evals-cicd-basic](https://github.com/langchain-samples/evals-cicd-basic) from the LangChain samples collection.

## Run It

Follow the [playbook](playbook.md).

## Why Start Here

The cleanest introduction to the core question: *how do you know your agent is good enough to merge?* No deployment, no infrastructure — just the evaluation pattern in its simplest form.
