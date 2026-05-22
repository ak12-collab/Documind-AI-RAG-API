from fastapi import FastAPI

from app.routes.query import router as query_router
from app.routes.upload import router as upload_router

app = FastAPI()

app.include_router(query_router)
app.include_router(upload_router)

@app.get("/")
def home():
    return {"message": "Production-style RAG API running"}