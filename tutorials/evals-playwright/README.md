# Evals with Playwright — Browser-Based UI Testing

Evaluate LLM applications through their web UI using Playwright browser automation. Designed for cases where there is no direct API — the agent is accessed through a chat interface in a browser.

## What It Covers

- Playwright browser automation against a live chat UI
- Clipboard-based response extraction for streamed outputs
- LLM-as-judge correctness evaluation via LangSmith
- Extensible response format models (Pydantic)
- Headless mode, configurable timeouts, rate limiting

## Source

Based on [langsmith-evals-playwright](https://github.com/langchain-samples/langsmith-evals-playwright) from the LangChain samples collection.

## Run It

Follow the [playbook](playbook.md).

## When This Is Relevant

When the LLM application is only accessible via a web UI — no SDK, no API endpoint. Playwright becomes the only way to automate evaluation at scale.
