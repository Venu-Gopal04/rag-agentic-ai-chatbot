# Agentic RAG Chatbot (Python)

This project is an **Agentic AI-based Retrieval-Augmented Generation (RAG) chatbot**
built using **Python, LangChain, ChromaDB, and HuggingFace embeddings**.

The chatbot ingests a PDF document, converts it into vector embeddings, stores them
in a vector database, and allows users to ask questions grounded strictly in the
document content.

---

## 🧠 Architecture Overview

PDF → Text Splitting → Embeddings → ChromaDB → Similarity Search → Response

### Components
- **PDF Loader**: Reads the PDF document
- **Text Splitter**: Breaks text into manageable chunks
- **Embeddings**: Converts text into vector representations
- **Vector DB (ChromaDB)**: Stores and retrieves vectors
- **Query Engine**: Returns answers with retrieved context and confidence scores

---

## 🛠 Tech Stack

- Python
- LangChain
- ChromaDB
- HuggingFace Sentence Transformers
- PyPDF

---

## ⚙️ Setup Instructions

>1. Clone the repository
git clone https://github.com/Venu-Gopal04/rag-agentic-ai-chatbot.git
cd rag-agentic-ai-chatbot
>2. Create and activate virtual environment
    python -m venv venv
    For Windows:
    venv\Scripts\activate
>3. Install dependencies
    pip install -r requirements.txt


🚀 How to Run the Project
Step 1: Ingest the PDF

Place your PDF file inside the data/ folder, then run:

python ingest.py


This will:

Load the PDF

Split text into chunks

Generate embeddings

Store them in ChromaDB

Step 2: Query the chatbot
python query.py


You will be prompted to ask a question based on the PDF content.

📌 Output Format

Each query response includes:

Final Answer – The answer generated from the document

Retrieved Context Chunks – Relevant text sections used for the answer

Confidence Score – Similarity score from the vector database

This ensures transparency and grounding of responses.

🧪 Sample Queries

Here are some example questions you can ask:

What is Agentic AI?

How is Agentic AI different from traditional AI?

What problems does Agentic AI solve?

What are real-world use cases of Agentic AI?

What value does Agentic AI bring to businesses?

How does Agentic AI improve decision making?

🏗️ Short Architecture Explanation

This system follows a Retrieval-Augmented Generation (RAG) approach where documents
are first converted into vector embeddings and stored in a vector database. At query
time, relevant chunks are retrieved using similarity search and used to generate
accurate, context-aware responses grounded in the source document.

📂 Project Structure
rag-agentic-ai-chatbot/
│
├── data/              # PDF files
├── chroma_db/         # Vector database
├── ingest.py          # PDF ingestion pipeline
├── query.py           # Query interface
├── app.py             # (Optional) API / UI entry point
├── requirements.txt   # Dependencies
├── README.md          # Project documentation
└── .gitignore
