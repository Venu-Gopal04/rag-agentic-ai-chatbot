from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from sentence_transformers import SentenceTransformer
from langchain.embeddings.base import Embeddings


# ---- HuggingFace wrapper (stable, no langchain-huggingface needed) ----
class HFEmbeddings(Embeddings):
    def __init__(self, model_name="sentence-transformers/all-MiniLM-L6-v2"):
        self.model = SentenceTransformer(model_name)

    def embed_documents(self, texts):
        return self.model.encode(texts, show_progress_bar=True).tolist()

    def embed_query(self, text):
        return self.model.encode(text).tolist()


# ---- Load PDF ----
pdf_path = "data/Ebook-Agentic-AI.pdf"
loader = PyPDFLoader(pdf_path)
documents = loader.load()
print(f"PDF loaded with {len(documents)} pages")

# ---- Split text ----
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
chunks = text_splitter.split_documents(documents)
print(f"Total chunks created: {len(chunks)}")

# ---- Embeddings ----
embeddings = HFEmbeddings()

# ---- Store in Chroma ----
vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embeddings,
    persist_directory="chroma_db"
)

print("✅ Embeddings stored successfully in ChromaDB")
