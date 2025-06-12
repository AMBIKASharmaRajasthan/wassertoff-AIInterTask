import json
from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.utils import embedding_functions

# Load document texts
with open("document_texts.json") as f:
    all_docs = json.load(f)

model = SentenceTransformer("all-MiniLM-L6-v2")
embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name="all-MiniLM-L6-v2"
)

client = chromadb.Client()
collection = client.get_or_create_collection(
    name="wasserstoff_docs",
    embedding_function=embedding_function
)

def chunk_text(text, chunk_size=500):
    return [text[i:i+chunk_size] for i in range(0, len(text), chunk_size)]

for filename, content in all_docs.items():
    chunks = chunk_text(content)
    for i, chunk in enumerate(chunks):
        collection.add(
            documents=[chunk],
            metadatas=[{"source": filename, "chunk": i}],
            ids=[f"{filename}_{i}"]
        )

print("✅ Documents embedded and stored in ChromaDB")