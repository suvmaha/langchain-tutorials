import bs4
import requests
from langchain_core.documents import Document
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_text_splitters import RecursiveCharacterTextSplitter

from config import get_embeddings_config

# ── Embeddings config ─────────────────────────────────────────────────────────

cfg = get_embeddings_config()


def get_embeddings():
    provider = cfg["embeddings_provider"]
    model_name = cfg["embeddings_model"]
    if provider == "huggingface":
        from langchain_huggingface import HuggingFaceEmbeddings
        return HuggingFaceEmbeddings(model_name=model_name)
    elif provider == "openai":
        from langchain_openai import OpenAIEmbeddings
        return OpenAIEmbeddings(model=model_name)
    elif provider == "ollama":
        from langchain_ollama import OllamaEmbeddings
        return OllamaEmbeddings(model=model_name)
    raise ValueError(f"Unknown embeddings provider: {provider}")


# ── Indexing ──────────────────────────────────────────────────────────────────

def load_and_index() -> InMemoryVectorStore:
    print("Loading document...")
    bs4_strainer = bs4.SoupStrainer(class_=("post-title", "post-header", "post-content"))
    response = requests.get("https://lilianweng.github.io/posts/2023-06-23-agent/")
    response.raise_for_status()
    soup = bs4.BeautifulSoup(response.text, "html.parser", parse_only=bs4_strainer)
    docs = [Document(page_content=soup.get_text(), metadata={"source": "lilianweng-agent"})]
    print(f"  {len(docs[0].page_content):,} characters loaded")

    print("Splitting into chunks...")
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        add_start_index=True,
    )
    splits = splitter.split_documents(docs)
    print(f"  {len(splits)} chunks")

    print("Embedding and indexing...")
    embeddings = get_embeddings()
    vector_store = InMemoryVectorStore(embeddings)
    vector_store.add_documents(splits)
    print("  Done\n")
    return vector_store


# ── Search ────────────────────────────────────────────────────────────────────

def run_search(vector_store: InMemoryVectorStore, query: str, k: int = 4):
    print(f"\nQuery: {query}")
    print("-" * 60)
    results = vector_store.similarity_search_with_score(query, k=k)
    for i, (doc, score) in enumerate(results, 1):
        snippet = doc.page_content[:140].strip().replace("\n", " ")
        print(f"  [{i}] score={score:.3f}  {snippet}...")
    print()


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print(f"Embeddings : {cfg['embeddings_provider']}/{cfg['embeddings_model']}\n")

    vector_store = load_and_index()

    queries = [
        "What is Task Decomposition?",
        "What are the main types of memory in LLM agents?",
        "How does the ReAct framework work?",
    ]

    for q in queries:
        run_search(vector_store, q)
