from fastapi import APIRouter

from app.services.vector_store import collection
from app.services.llm_service import generate_response

router = APIRouter()

@router.get("/ask")
def ask(question: str, source: str = "resume"):

    results = collection.query(
        query_texts=[question],
        n_results=3,
        where={"source": source},
    )

    context = "\n\n".join(results["documents"][0])

    prompt = f"""
Use the context below to answer the question.

Context:
{context}

Question:
{question}
"""

    answer = generate_response(prompt)

    return {
        "question": question,
        "source": source,
        "answer": answer,
        "context_used": results["documents"][0],
    }