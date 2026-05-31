# Medicare AI Assistant

> RAG-powered chatbot for medical documents — ask questions about any medical PDF in plain English

[![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)](https://python.org)
[![LangChain](https://img.shields.io/badge/LangChain-1C3C3C?style=flat&logo=chainlink&logoColor=white)](https://langchain.com)
[![FAISS](https://img.shields.io/badge/FAISS-Vector_Search-blue?style=flat)](https://faiss.ai)
[![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)](https://streamlit.io)

---

## What It Does

Upload any medical PDF (research paper, clinical guidelines, patient records) and ask questions about it in plain English. The system uses Retrieval-Augmented Generation (RAG) to find the most relevant passages and generate accurate, grounded answers.

---

## Architecture

```
Medical PDF
    |
    v
PyPDF2 text extraction
    |
    v
Chunking (1000 chars, 200 overlap)
    |
    v
Sentence-Transformers embeddings
    |
    v
FAISS vector index
    |
    v
User question  ──>  similarity search  ──>  top-k chunks
                                                |
                                                v
                                           LLM (grounded answer)
                                                |
                                                v
                                       Streamlit chat interface
```

---

## Tech Stack

| Component | Technology |
|---|---|
| RAG Framework | LangChain |
| Vector Store | FAISS |
| Embeddings | Sentence-Transformers |
| LLM | OpenAI / EuriAI |
| Frontend | Streamlit |
| PDF Parsing | PyPDF2 |

---

## Setup

```bash
git clone https://github.com/smithparekh/medicare-ai-assistant
cd medicare-ai-assistant
pip install -r requirements.txt

# Add your API key
export EURI_API_KEY=your_key_here

streamlit run main.py
```

---

## Key Features

- Full RAG pipeline with chunk overlap for context continuity
- Session state management for multi-turn conversations
- Clean Streamlit chat UI with message history
- Supports any PDF — not limited to medical documents
