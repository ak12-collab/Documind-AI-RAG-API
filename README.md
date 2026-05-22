````markdown
# 🚀 AI Knowledge Retrieval API (RAG API)

An advanced **Retrieval-Augmented Generation (RAG)** backend engineered using **FastAPI, ChromaDB, Ollama, and semantic embeddings**.

This system enables users to upload PDF documents, generate vector embeddings, perform semantic similarity search, and receive accurate, context-aware AI-generated responses using local LLM inference pipelines.

---

# ✨ Features

✅ FastAPI-powered REST API  
✅ Local LLM inference using Ollama  
✅ ChromaDB vector database integration  
✅ Semantic embeddings with `nomic-embed-text`  
✅ PDF upload and ingestion pipeline  
✅ Intelligent text chunking  
✅ High-performance vector similarity search  
✅ Metadata-based document filtering  
✅ Context-aware AI response generation  
✅ Modular and scalable backend architecture  

---

# 🧠 System Architecture

```text
👤 User Query
        │
        ▼
⚡ FastAPI Endpoint
        │
        ▼
🧩 Embedding Model
        │
        ▼
🗂️ ChromaDB Vector Search
        │
        ▼
📚 Context Retrieval
        │
        ▼
📝 Prompt Augmentation
        │
        ▼
🤖 LLM Response Generation
```

---

# 🛠️ Tech Stack

| Technology | Purpose |
|---|---|
| 🐍 Python | Core backend language |
| ⚡ FastAPI | API framework |
| 🧠 Ollama | Local LLM inference |
| 🗂️ ChromaDB | Vector database |
| 📄 PyMuPDF | PDF text extraction |
| 🚀 Uvicorn | ASGI server |
| 🤖 Mistral | Large Language Model |
| 🔍 nomic-embed-text | Embedding model |

---

# 📁 Project Structure

```bash
rag-api/
│
├── app/
│   ├── routes/
│   ├── services/
│   ├── utils/
│   └── config/
│
├── uploads/
├── chroma_db/
├── requirements.txt
└── README.md
```

---

# 🔌 API Endpoints

## 📤 Upload PDF

### `POST /upload`

Uploads PDF documents, extracts text, generates semantic embeddings, and stores vector data inside ChromaDB.

---

## 💬 Ask Questions

### `GET /ask`

Retrieves relevant document chunks using semantic vector search and generates grounded AI responses.

### Example Request

```bash
/ask?question=Summarize the uploaded PDF&source=resume
```

---

# ⚙️ Setup Instructions

## 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/rag-api.git

cd rag-api
```

---

## 2️⃣ Create Virtual Environment

```bash
python -m venv venv

.\venv\Scripts\Activate.ps1
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 4️⃣ Pull Ollama Models

```bash
ollama pull mistral

ollama pull nomic-embed-text
```

---

## 5️⃣ Run Application

```bash
uvicorn app.main:app --reload
```

---

# 📚 Swagger API Documentation

```bash
http://127.0.0.1:8000/docs
```

---

# 🚀 Future Enhancements

🔹 Advanced chunking strategies  
🔹 Streaming AI responses  
🔹 Multi-document semantic querying  
🔹 Authentication & authorization  
🔹 Dockerized deployment pipeline  
🔹 Qdrant vector database support  
🔹 Hybrid search implementation  
🔹 Production monitoring & observability  

---

# 💼 Resume Highlights

✅ Built a production-style Retrieval-Augmented Generation (RAG) API using FastAPI, ChromaDB, and Ollama.  

✅ Implemented PDF ingestion pipelines, semantic embeddings, vector similarity search, and grounded AI response workflows.  

✅ Designed a modular backend architecture with reusable service layers, API routes, and scalable retrieval pipelines.  

✅ Integrated local LLM inference using Mistral with semantic retrieval workflows for context-aware AI interactions.  

✅ Developed an end-to-end AI knowledge retrieval system optimized for scalable document intelligence applications.  

---

# 🧩 Core Capabilities

```text
📄 PDF Processing
🔍 Semantic Search
🧠 AI Question Answering
⚡ Local LLM Inference
🗂️ Vector Database Retrieval
🚀 FastAPI Backend Services
```

---

# 📌 Use Cases

💡 AI-powered document assistants  
💡 Enterprise knowledge retrieval systems  
💡 Resume and profile analyzers  
💡 Research paper summarization  
💡 Internal company knowledge bots  
💡 Offline/private AI document querying systems  
````
