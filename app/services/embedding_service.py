from chromadb.utils.embedding_functions.ollama_embedding_function import (
    OllamaEmbeddingFunction,
)

from app.config.settings import OLLAMA_URL, EMBED_MODEL

embedding_function = OllamaEmbeddingFunction(
    model_name=EMBED_MODEL,
    url=OLLAMA_URL,
)