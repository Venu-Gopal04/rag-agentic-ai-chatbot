# Agentic RAG Chatbot (Python)

This project is an Agentic AI-based Retrieval-Augmented Generation (RAG) chatbot built using **Python, LangChain, ChromaDB, and HuggingFace embeddings**.

The chatbot ingests a PDF document, converts it into vector embeddings, stores them in a vector database, and allows users to ask questions grounded strictly in the document content.

---

>Project Architecture

PDF → Text Splitting → Embeddings → ChromaDB → Query → Response

---

>Tech Stack

- Python
- LangChain
- ChromaDB
- HuggingFace Sentence Transformers
- PyPDF

---

>Setup Instructions

>1. Clone the repository
```bash
git clone https://github.com/Venu-Gopal04/rag-agentic-ai-chatbot.git
cd rag-agentic-ai-chatbot

>2. Install dependencies

pip install -r requirements.txt

3. Run the project

python ingest.py

python query.py
