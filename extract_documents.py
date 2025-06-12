import os
import pytesseract
from pdf2image import convert_from_path
from PyPDF2 import PdfReader
from pathlib import Path
import json
import zipfile

# path to Tesseract on Windows
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def extract_text_from_pdf(pdf_path):
    try:
        text = ""
        with open(pdf_path, 'rb') as f:
            reader = PdfReader(f)
            for page in reader.pages:
                text += page.extract_text() or ""
        if not text.strip():
            raise ValueError("No text, fallback to OCR")
        return text.strip()
    except:
        images = convert_from_path(pdf_path)
        ocr_text = ""
        for img in images:
            ocr_text += pytesseract.image_to_string(img)
        return ocr_text

def unzip_archive(zip_path, extract_to):
    os.makedirs(extract_to, exist_ok=True)
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        for file in zip_ref.namelist():
            if file.endswith(".pdf") or file.endswith(".txt"):
                print(f"🗂️ Extracting: {file}")
                zip_ref.extract(file, extract_to)
    print("✅ Archive extracted.")

def process_documents(input_dir, output_json):
    all_docs = {}
    docs_dir = Path(input_dir)
    for file in docs_dir.glob("*.pdf"):
        print(f"🔍 Processing: {file.name}")
        all_docs[file.name] = extract_text_from_pdf(str(file))
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(all_docs, f, indent=2)
    print(f"✅ Extraction complete. Saved to {output_json}")

# Example
if __name__ == "__main__":
    zip_path = "archive.zip"
    extract_folder = "documents"
    output_json = "document_texts.json"

    unzip_archive(zip_path, extract_folder)
    process_documents(extract_folder, output_json)
