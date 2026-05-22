import os

from fastapi import APIRouter, UploadFile, File

from app.services.pdf_service import extract_text_from_pdf
from app.utils.chunking import chunk_text
from app.services.vector_store import collection

router = APIRouter()

UPLOAD_DIR = "uploads"

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):

    file_path = os.path.join(UPLOAD_DIR, file.filename)

    # Save uploaded PDF
    with open(file_path, "wb") as buffer:
        buffer.write(await file.read())

    # Extract text
    text = extract_text_from_pdf(file_path)

    # Chunk text
    chunks = chunk_text(text)

    # Store chunks in ChromaDB
    collection.add(
        ids=[f"{file.filename}_{i}" for i in range(len(chunks))],
        documents=chunks,
        metadatas=[
            {
		"source": "resume",
		"filename": file.filename,
                "chunk": i,
            }
            for i in range(len(chunks))
        ],
    )

    return {
        "message": f"{file.filename} uploaded successfully",
        "chunks_stored": len(chunks),
    }