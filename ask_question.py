from groq import Groq
import chromadb
from chromadb.utils import embedding_functions
from sentence_transformers import SentenceTransformer

# API Key
GROQ_API_KEY = "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"  
client = Groq(api_key=GROQ_API_KEY)

# Load embedding model
model_name = "all-MiniLM-L6-v2"
embedder = SentenceTransformer(model_name)
embedding_function = embedding_functions.SentenceTransformerEmbeddingFunction(
    model_name=model_name
)

# Connect to ChromaDB collection
vector_client = chromadb.Client()
collection = vector_client.get_or_create_collection(
    name="wasserstoff_docs",
    embedding_function=embedding_function
)

def ask_question(query):
    results = collection.query(query_texts=[query], n_results=5)
    documents = results["documents"][0]
    metadatas = results["metadatas"][0]

    context = "\n\n".join([
        f"{doc}\n(Source: {meta['source']}, Chunk: {meta['chunk']})"
        for doc, meta in zip(documents, metadatas)
    ])

    prompt = f"""
You're an intelligent assistant. Read the document snippets below and answer the user's query with clear citations.

Context:
{context}

Question: {query}
Answer:
"""

    response = client.chat.completions.create(
        model="llama3-70b-8192",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content, documents, metadatas