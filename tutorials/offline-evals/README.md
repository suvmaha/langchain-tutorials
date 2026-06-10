# Offline Evals — Production Grade

Daily automated evaluation pipeline for financial agents. Combines multiple evaluation types — trajectory matching, LLM-as-judge, tool argument validation — with dataset versioning, scheduled cron runs, and Slack notifications.

## What It Covers

- Two financial agents: Portfolio Agent and Market Data Agent
- Four evaluation types: trajectory match, LLM-judge correctness, custom relevance, tool/args validation
- Daily cron pipeline with dataset versioning (daily-YYYY-MM-DD tags)
- GitHub Actions 4-job pipeline: update datasets → run evals → generate report → Slack notification
- Criteria-based thresholds per evaluator

## Source

Based on [offline-evals-cicd](https://github.com/langchain-samples/offline-evals-cicd) from the LangChain samples collection.

## Run It

Follow the [playbook](playbook.md).

## Why This Matters

Production agents need ongoing monitoring, not just pre-deploy checks. This shows how to run evaluations continuously against fresh data — the same pattern used in production ML systems.
