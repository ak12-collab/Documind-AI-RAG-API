import chromadb

from app.config.settings import (
    CHROMA_PATH,
    COLLECTION_NAME,
)

from app.services.embedding_service import embedding_function

client = chromadb.PersistentClient(path=CHROMA_PATH)

collection = client.get_or_create_collection(
    name=COLLECTION_NAME,
    embedding_function=embedding_function,
)
