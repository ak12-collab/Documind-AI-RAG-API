from fastapi import FastAPI
import ollama
import chromadb

from chromadb.utils.embedding_functions.ollama_embedding_function import (
    OllamaEmbeddingFunction,
)

app = FastAPI()

# Connect to ChromaDB
client = chromadb.PersistentClient(path="./chroma_db")

# Embedding function
ef = OllamaEmbeddingFunction(
    model_name="nomic-embed-text",
    url="http://localhost:11434",
)

# Load collection
collection = client.get_or_create_collection(
    name="personal_profile",
    embedding_function=ef,
)

@app.get("/")
def home():
    return {"message": "RAG API running"}

@app.get("/ask")
def ask(question: str):

    # Retrieve relevant chunks
    results = collection.query(
        query_texts=[question],
        n_results=2,
    )

    # Build context
    context = "\n\n".join(results["documents"][0])

    # Augmented prompt
    prompt = f"""
Use the context below to answer the question.

Context:
{context}

Question:
{question}
"""

    # Generate response
    response = ollama.chat(
        model="qwen2.5:0.5b",
        messages=[
            {
                "role": "user",
                "content": prompt,
            }
        ],
    )

    return {
        "question": question,
        "answer": response["message"]["content"],
        "context_used": results["documents"][0],
    }