<div align="center">

# 🧠 Documind-AI-RAG API 

**A production-grade Retrieval-Augmented Generation backend powered by FastAPI, ChromaDB, and local LLM inference.**

[![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=for-the-badge&logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com)
[![ChromaDB](https://img.shields.io/badge/ChromaDB-Vector_DB-FF6B35?style=for-the-badge)](https://www.trychroma.com)
[![Ollama](https://img.shields.io/badge/Ollama-Local_LLM-000000?style=for-the-badge)](https://ollama.ai)
[![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)](LICENSE)

<br/>

> *Upload documents. Ask questions. Get intelligent, context-aware answers — entirely offline.*

</div>

---

## 📌 Overview

**Documind-AI-RAG API** is an end-to-end AI knowledge retrieval system that allows users to upload PDF documents, generate semantic vector embeddings, and query them using a local LLM no cloud, no data leakage, no API keys required.

It combines **semantic similarity search** with **prompt augmentation** to deliver accurate, grounded responses from your own document corpus.

---

## ✨ Key Features

| Feature | Description |
|---|---|
| 📄 **PDF Ingestion** | Upload and parse PDFs into searchable text chunks |
| 🔍 **Semantic Search** | High-accuracy vector similarity search via ChromaDB |
| 🧠 **Local LLM Inference** | Private, offline AI responses using Ollama + Mistral |
| ⚡ **FastAPI Backend** | High-performance async REST API with auto-generated docs |
| 🧩 **Modular Architecture** | Clean separation of routes, services, and utilities |
| 🗂️ **Metadata Filtering** | Filter document chunks by source, type, or custom tags |
| 🔒 **Privacy First** | 100% local execution — your data never leaves your machine |

---

## 🏗️ System Architecture

```
┌──────────────────────────────────────────────────────────┐
│          Documind-AI-RAG API Pipeline                    │
├──────────────────────────────────────────────────────────┤
│                                                          │
│   👤 User Query                                          │
│        │                                                 │
│        ▼                                                 │
│   ⚡ FastAPI Endpoint      ◄──── 📤 PDF Upload           │
│        │                              │                  │
│        ▼                              ▼                  │
│   🔍 nomic-embed-text       🧩 Text Chunking             │
│   (Query Embedding)         + Embedding                  │
│        │                              │                  │
│        └──────────► 🗂️ ChromaDB ◄────┘                  │
│                       Vector Store                       │
│                          │                               │
│                          ▼                               │
│                   📚 Top-K Context Retrieval             │
│                          │                               │
│                          ▼                               │
│                   📝 Prompt Augmentation                 │
│                          │                               │
│                          ▼                               │
│                   🤖 Mistral (Ollama)                    │
│                   Response Generation                    │
│                          │                               │
│                          ▼                               │
│                   💬 Grounded AI Answer                  │
└──────────────────────────────────────────────────────────┘
```

---

## 🛠️ Tech Stack

| Layer | Technology | Role |
|---|---|---|
| **Language** | 🐍 Python 3.10+ | Core backend |
| **API Framework** | ⚡ FastAPI | REST endpoints, routing |
| **ASGI Server** | 🚀 Uvicorn | High-performance async serving |
| **LLM Engine** | 🤖 Ollama + Mistral | Local language model inference |
| **Embedding Model** | 🔍 nomic-embed-text | Semantic vector generation |
| **Vector Database** | 🗂️ ChromaDB | Embedding storage & retrieval |
| **PDF Processing** | 📄 PyMuPDF | Text extraction from PDFs |

---

## 📁 Project Structure

```bash
rag-api/
│
├── app/
│   ├── routes/          # API endpoint definitions
│   ├── services/        # Core business logic (RAG pipeline)
│   ├── utils/           # Helpers (chunking, embeddings, formatting)
│   └── config/          # App settings and environment config
│
├── uploads/             # Uploaded PDF storage
├── chroma_db/           # Persistent ChromaDB vector store
├── requirements.txt
└── README.md
```

---

## 🔌 API Reference

### `POST /upload` — Ingest a PDF

Uploads a PDF document, extracts and chunks text, generates semantic embeddings, and stores vectors in ChromaDB.

```bash
curl -X POST "http://127.0.0.1:8000/upload" \
  -F "file=@your_document.pdf"
```

---

### `GET /ask` — Query Your Documents

Performs semantic vector search over ingested documents and returns a context-grounded AI response.

```bash
GET /ask?question=Summarize the uploaded document&source=resume
```

**Response:**
```json
{
  "answer": "Based on the document, ...",
  "sources": ["resume_chunk_3", "resume_chunk_7"]
}
```

📖 Full interactive docs available at: `http://127.0.0.1:8000/docs`

---

## ⚙️ Getting Started

### Prerequisites
- Python 3.10+
- [Ollama](https://ollama.ai) installed and running

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/rag-api.git
cd rag-api
```

### 2. Set Up a Virtual Environment

```bash
python -m venv venv
.\venv\Scripts\Activate.ps1        # Windows
# source venv/bin/activate          # macOS/Linux
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Pull Required Ollama Models

```bash
ollama pull mistral
ollama pull nomic-embed-text
```

### 5. Launch the API

```bash
uvicorn app.main:app --reload
```

The API will be live at `http://127.0.0.1:8000` 🎉

---

## 💼 Resume Highlights

- 🏗️ **Architected** a production-style RAG system using FastAPI, ChromaDB, and Ollama with a clean, modular service layer
- 📄 **Built** a full PDF ingestion pipeline from text extraction and intelligent chunking to embedding generation and vector storage
- 🔍 **Implemented** semantic similarity search using ChromaDB with metadata-based filtering for precise document retrieval
- 🤖 **Integrated** local LLM inference (Mistral via Ollama) into a prompt-augmented response generation workflow
- 🔒 **Designed** for full offline operation zero cloud dependencies, ensuring enterprise-grade data privacy

---

## 🗺️ Roadmap

- [ ] 🌊 Streaming AI responses
- [ ] 🔐 Authentication & authorization (JWT)
- [ ] 🐳 Dockerized deployment pipeline
- [ ] 📊 Production monitoring & observability (Prometheus + Grafana)
- [ ] 🔀 Hybrid search (vector + keyword BM25)
- [ ] 📁 Multi-document cross-source querying
- [ ] 🗄️ Qdrant vector database support
- [ ] 🧩 Advanced chunking strategies (semantic, hierarchical)

---

## 💡 Use Cases

> This system is designed for any scenario where you need **private, intelligent document Q&A**.

- 🏢 Enterprise internal knowledge base assistants
- 📑 Research paper & report summarization
- 👤 Resume and professional profile analyzers
- 🔒 Offline/air-gapped document intelligence systems
- 🤖 Custom AI chatbots over proprietary documentation

---

<div align="center">

**Built with ❤️ using FastAPI · ChromaDB · Ollama · Mistral**

*If you found this useful, please consider ⭐ starring the repo!*

</div>
