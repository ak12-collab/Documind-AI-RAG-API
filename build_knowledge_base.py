import chromadb
from chromadb.utils.embedding_functions.ollama_embedding_function import (
    OllamaEmbeddingFunction,
)

# Load profile
with open("profile.txt", "r", encoding="utf-8") as f:
    text = f.read()

# Split text into chunks
chunks = [chunk.strip() for chunk in text.split("\n\n") if chunk.strip()]

print(f"Loaded {len(chunks)} chunks")

# Create ChromaDB client
client = chromadb.PersistentClient(path="./chroma_db")

# Embedding function using Ollama
ef = OllamaEmbeddingFunction(
    model_name="nomic-embed-text",
    url="http://localhost:11434",
)

# Create collection
collection = client.get_or_create_collection(
    name="personal_profile",
    embedding_function=ef,
)

# Add chunks
collection.add(
    ids=[f"chunk{i}" for i in range(len(chunks))],
    documents=chunks,
    metadatas=[{"chunk": i} for i in range(len(chunks))],
)

print("Knowledge base built successfully!")