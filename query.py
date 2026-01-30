from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

# Load the same embedding model used during ingestion
embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load existing ChromaDB
vectordb = Chroma(
    persist_directory="chroma_db",
    embedding_function=embedding
)

print("Vector database loaded successfully ✅")

# Ask a question
query = input("\nAsk a question from the PDF: ")

# Retrieve top 3 relevant chunks
docs = vectordb.similarity_search(query, k=3)

print("\n📄 Answer (from PDF content):\n")

for i, doc in enumerate(docs, 1):
    print(f"--- Result {i} ---")
    print(doc.page_content)
    print()
