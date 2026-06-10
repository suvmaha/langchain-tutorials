import os

PRESETS = {
    "ollama-full": {
        "llm_provider": "ollama",
        "llm_model": os.getenv("LLM_MODEL", "llama3.2"),
        "embeddings_provider": "ollama",
        "embeddings_model": os.getenv("EMBEDDINGS_MODEL", "nomic-embed-text"),
    },
    "ollama": {
        "llm_provider": "ollama",
        "llm_model": os.getenv("LLM_MODEL", "llama3.2"),
        "embeddings_provider": "huggingface",
        "embeddings_model": os.getenv("EMBEDDINGS_MODEL", "all-MiniLM-L6-v2"),
    },
    "anthropic": {
        "llm_provider": "anthropic",
        "llm_model": os.getenv("LLM_MODEL", "claude-haiku-4-5-20251001"),
        "embeddings_provider": "huggingface",
        "embeddings_model": os.getenv("EMBEDDINGS_MODEL", "all-MiniLM-L6-v2"),
    },
    "openai": {
        "llm_provider": "openai",
        "llm_model": os.getenv("LLM_MODEL", "gpt-4o-mini"),
        "embeddings_provider": "openai",
        "embeddings_model": os.getenv("EMBEDDINGS_MODEL", "text-embedding-3-small"),
    },
}


def get_model_config() -> dict:
    preset = os.getenv("MODEL_PRESET", "ollama-full")
    if preset not in PRESETS:
        raise ValueError(
            f"Unknown MODEL_PRESET '{preset}'. Choose from: {list(PRESETS.keys())}"
        )
    return PRESETS[preset]
