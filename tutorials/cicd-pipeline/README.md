# CI/CD Pipeline — Code to Production

Full code-to-production pipeline for a LangGraph agent. A Text-to-SQL agent (natural language → SQL → answer) with a complete GitHub Actions pipeline: lint, unit tests, integration tests, E2E tests, LLM evaluations, preview deployment, production deployment.

## What It Covers

- LangGraph 3-node linear agent (generate_sql → execute_sql → generate_answer)
- Multi-layer testing: unit → integration → E2E → offline evals
- LLM-as-judge with multiple evaluators and thresholds
- Docker image build and push
- Preview deployment per PR, production on merge
- LangGraph Platform control plane API

## Source

Based on [cicd-pipeline-example](https://github.com/langchain-samples/cicd-pipeline-example) from the LangChain samples collection.

## Run It

Follow the [playbook](playbook.md).

## Why This Matters

Adds deployment to the evaluation pattern — the quality gate now blocks a real ship decision, not just a PR comment.
