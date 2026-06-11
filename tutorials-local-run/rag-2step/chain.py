import bs4
import requests
from langchain_core.documents import Document
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain.chat_models import init_chat_model

from config import get_model_config

# ── Model config ──────────────────────────────────────────────────────────────

cfg = get_model_config()
model = init_chat_model(cfg["llm_model"], model_provider=cfg["llm_provider"])


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


# ── Chain ─────────────────────────────────────────────────────────────────────

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)


def make_chain(vector_store: InMemoryVectorStore):
    retriever = vector_store.as_retriever(search_kwargs={"k": 4})

    prompt = ChatPromptTemplate.from_messages([
        (
            "system",
            "Answer the question using only the provided context. "
            "If the context does not contain the answer, say you don't know.\n\n"
            "Context:\n{context}",
        ),
        ("human", "{question}"),
    ])

    gen_chain = prompt | model | StrOutputParser()

    return retriever, gen_chain


# ── Query runner ──────────────────────────────────────────────────────────────

def run_query(retriever, gen_chain, query: str):
    print(f"\nQ: {query}")
    print("-" * 60)

    # Step 1: Retrieve
    docs = retriever.invoke(query)
    print(f"  [Step 1 — Retrieved {len(docs)} chunks]")
    for i, doc in enumerate(docs, 1):
        snippet = doc.page_content[:120].strip().replace("\n", " ")
        print(f"    {i}. {snippet}...")

    # Step 2: Generate
    context = format_docs(docs)
    answer = gen_chain.invoke({"context": context, "question": query})
    print(f"\nA: {answer}")


# ── Main ──────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    print(f"LLM        : {cfg['llm_provider']}/{cfg['llm_model']}")
    print(f"Embeddings : {cfg['embeddings_provider']}/{cfg['embeddings_model']}\n")

    vector_store = load_and_index()
    retriever, gen_chain = make_chain(vector_store)

    questions = [
        "What is Task Decomposition?",
        "What are the main types of memory in LLM agents?",
    ]

    for q in questions:
        run_query(retriever, gen_chain, q)
