# RAG — 2-Step (Retrieve then Generate)

## References

- https://docs.langchain.com/oss/python/langchain/rag
- https://docs.langchain.com/oss/python/langchain/retrieval

Simple, predictable RAG pattern. You control retrieval — the LLM never decides whether or when to retrieve. Always retrieves, always generates.

## What It Covers

- Document loading and chunking
- Embeddings and vector store (FAISS or Chroma)
- Similarity search: query → top-k relevant chunks
- LLM generation with retrieved chunks as context

## The Pattern

```
User query
    ↓
Retrieve top-k chunks from vector store
    ↓
Stuff chunks into LLM prompt as context
    ↓
LLM generates answer
```

## When to Use

- Unstructured text (PDFs, docs, articles)
- You always want retrieval — no need for the LLM to decide
- Simpler, faster, more predictable than Agentic RAG

## When NOT to Use

- You already have a SQL database or structured data — query it directly instead
- You need multi-step reasoning or multiple retrieval rounds — use Agentic RAG

## Framework

LangChain

## Prerequisites

- Python + API key (Anthropic or OpenAI)
- No cluster or cloud needed — runs locally
