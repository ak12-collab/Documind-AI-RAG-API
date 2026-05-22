\# AI Knowledge Retrieval API (RAG API)



An AI-powered Retrieval-Augmented Generation (RAG) backend built using FastAPI, ChromaDB, Ollama, and semantic embeddings.



This project enables users to upload PDFs, generate embeddings, perform semantic vector search, and receive context-aware AI responses using local LLM inference.



\---



\# Features



\* FastAPI backend API

\* Local LLM inference using Ollama

\* ChromaDB vector database

\* Semantic embeddings using nomic-embed-text

\* PDF upload and ingestion

\* Automatic chunking

\* Vector similarity search

\* Metadata filtering

\* Context-aware AI responses

\* Modular backend architecture



\---



\# Architecture



User Query

↓

FastAPI Endpoint

↓

Embedding Model

↓

ChromaDB Vector Search

↓

Context Retrieval

↓

Prompt Augmentation

↓

LLM Response



\---



\# Tech Stack



\* Python

\* FastAPI

\* Ollama

\* ChromaDB

\* PyMuPDF

\* Uvicorn

\* Mistral

\* nomic-embed-text



\---



\# Folder Structure



rag-api/

│

├── app/

│   ├── routes/

│   ├── services/

│   ├── utils/

│   └── config/

│

├── uploads/

├── chroma\_db/

├── requirements.txt

└── README.md



\---



\# API Endpoints



\## Upload PDF



POST /upload



Uploads PDF documents, extracts text, generates embeddings, and stores vectors in ChromaDB.



\---



\## Ask Questions



GET /ask



Retrieves relevant chunks using semantic search and generates grounded AI responses.



Example:



/ask?question=Summarize the uploaded PDF\&source=resume



\---



\# Setup Instructions



\## Clone Repository



git clone <your-repo-url>



cd rag-api



\---



\## Create Virtual Environment



python -m venv venv



.\\venv\\Scripts\\Activate.ps1



\---



\## Install Dependencies



pip install -r requirements.txt



\---



\## Pull Ollama Models



ollama pull mistral



ollama pull nomic-embed-text



\---



\## Run Application



uvicorn app.main:app --reload



\---



\# Swagger API Docs



http://127.0.0.1:8000/docs



\---



\# Future Improvements



\* Better chunking strategies

\* Streaming responses

\* Multi-document querying

\* Authentication

\* Docker deployment

\* Qdrant vector database support



\---



\# Resume Highlights



\* Built a production-style Retrieval-Augmented Generation (RAG) API using FastAPI, ChromaDB, and Ollama.

\* Implemented PDF ingestion, semantic embeddings, vector similarity search, and grounded AI responses.

\* Designed modular backend architecture with reusable service and routing layers.

\* Integrated local LLM inference pipelines using Mistral and semantic retrieval workflows.



