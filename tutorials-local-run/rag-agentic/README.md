# Agentic RAG

## References

- https://docs.langchain.com/oss/python/langchain/rag
- https://docs.langchain.com/oss/python/langchain/retrieval

RAG where the agent decides whether to retrieve, what to retrieve, and whether to retrieve again. Built with LangGraph for full control over the reasoning loop.

## What It Covers

- Retrieval as a tool the agent chooses to call
- Multi-step retrieval: agent can retrieve multiple times
- Reflection: agent evaluates if it has enough information
- LangGraph nodes for retrieve, grade, generate, and decide

## The Pattern

```
User query
    ↓
Agent decides: do I need to retrieve?
    ↓ yes
Retrieve from vector store
    ↓
Agent grades: are these chunks relevant?
    ↓ not good enough → retrieve again with different query
    ↓ good enough
Generate answer
```

## When to Use

- Complex questions requiring multiple retrieval rounds
- You want the agent to rewrite the query if results are poor
- Multiple knowledge sources the agent picks between
- You need grounding checks before generating

## When NOT to Use

- Simple single-round retrieval — use 2-Step RAG instead
- Latency is critical — agentic loop adds LLM calls

## Framework

LangGraph

## Prerequisites

- Python + API key (Anthropic or OpenAI)
- No cluster or cloud needed — runs locally
