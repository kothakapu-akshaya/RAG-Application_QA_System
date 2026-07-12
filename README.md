# 📄 RAG Document Question Answering System

## Overview

The RAG (Retrieval-Augmented Generation) Document Question Answering System allows users to upload PDF documents and ask questions based on their content. The application retrieves relevant information from the uploaded document and generates answers using a locally running Large Language Model (LLM).

## Features

- Upload PDF documents
- Extract text using PyMuPDF4LLM
- Split text into semantic chunks
- Generate embeddings using SentenceTransformers
- Store embeddings in FAISS
- Retrieve relevant document chunks
- Generate answers using Ollama (phi3:mini)
- Interactive React-based chat interface

## Tech Stack

### Frontend

- React
- TypeScript
- Vite
- Axios

### Backend

- Python
- FastAPI

### RAG Components

- PyMuPDF4LLM – PDF text extraction
- LangChain RecursiveCharacterTextSplitter – Text chunking
- SentenceTransformers (all-MiniLM-L6-v2) – Embedding generation
- FAISS – Vector database
- Ollama (phi3:mini) – Local LLM for answer generation

## Workflow

1. Upload a PDF document.
2. Extract text using PyMuPDF4LLM.
3. Split the extracted text into chunks.
4. Generate embeddings for each chunk.
5. Store embeddings in FAISS.
6. Convert the user's question into an embedding.
7. Retrieve the most relevant chunks.
8. Generate an answer using Ollama (phi3:mini).
9. Display the answer in the frontend.


## API Endpoints

| Method | Endpoint | Description |             
|-------------|---------------|------------------|  
|**POST**     |`/upload`      | Upload a PDF document |  
| **POST** | `/query` | Ask questions about the uploaded document |  
| **GET** | `/health` | Check whether the backend service is running |


## Installation

### Backend

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload --port 8001
```

### Frontend

```bash
cd frontend
npm install
npm run dev
```

## Future Improvements

- Support multiple document uploads
- Improve retrieval accuracy
- Add chat history
- Support DOCX and TXT files
- Stream LLM responses


## Team Members

- Vanamoju Lakshmi Meghana
- Kothakapu Akshaya