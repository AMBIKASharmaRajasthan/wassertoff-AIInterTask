# 📚 Wasserstoff Gen-AI Chatbot

This project is a document research and theme identification chatbot built as part of the Wasserstoff AI Internship Task. It allows users to upload PDF or text documents, ask questions, and get accurate, cited answers along with synthesized themes across multiple documents.

---

## 🚀 Features

- ✅ Upload 75+ documents (.pdf, .txt, scanned)
- ✅ OCR support using Tesseract for scanned PDFs
- ✅ Embeds documents into ChromaDB using Sentence Transformers
- ✅ Semantic search and document retrieval
- ✅ Synthesized LLM answers with citations (document + chunk)
- ✅ Clean Streamlit UI for uploading, querying, and viewing results
- ✅ Modular and well-commented codebase

---

## 🛠️ Tech Stack

| Layer         | Technology                     |
|---------------|--------------------------------|
| Language Model| Groq LLaMA3 (via `groq` SDK)   |
| Embedding     | `sentence-transformers` (MiniLM)|
| Vector Store  | `ChromaDB`                     |
| OCR           | `Tesseract OCR` + `pdf2image`  |
| UI            | `Streamlit`                    |
| Backend       | Python                         |

---

## 📂 Project Structure

