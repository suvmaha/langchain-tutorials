import os

PRESETS = {
    "huggingface": {
        "embeddings_provider": "huggingface",
        "embeddings_model": os.getenv("EMBEDDINGS_MODEL", "all-MiniLM-L6-v2"),
    },
    "ollama": {
        "embeddings_provider": "ollama",
        "embeddings_model": os.getenv("EMBEDDINGS_MODEL", "nomic-embed-text"),
    },
    "openai": {
        "embeddings_provider": "openai",
        "embeddings_model": os.getenv("EMBEDDINGS_MODEL", "text-embedding-3-small"),
    },
}


def get_embeddings_config() -> dict:
    preset = os.getenv("EMBEDDINGS_PRESET", "huggingface")
    if preset not in PRESETS:
        raise ValueError(
            f"Unknown EMBEDDINGS_PRESET '{preset}'. Choose from: {list(PRESETS.keys())}"
        )
    return PRESETS[preset]
