# app/parser.py

from pdfminer.high_level import extract_text as extract_pdf_text
from docx import Document
from typing import Union
from PIL import Image
import pytesseract
import os

SUPPORTED_TYPES = ["pdf", "docx", "jpg", "jpeg", "png"]

def extract_text(file_path: str, file_type: str) -> Union[str, None]:
    file_type = file_type.lower()

    if file_type not in SUPPORTED_TYPES:
        raise ValueError(f"Unsupported file type: {file_type}")

    if file_type == "pdf":
        return extract_from_pdf(file_path)
    elif file_type == "docx":
        return extract_from_docx(file_path)
    elif file_type in ["jpg", "jpeg", "png"]:
        return extract_from_image(file_path)

    return None

def extract_from_pdf(file_path: str) -> str:
    try:
        return extract_pdf_text(file_path)
    except Exception as e:
        raise RuntimeError(f"Error extracting text from PDF: {e}")

def extract_from_docx(file_path: str) -> str:
    try:
        doc = Document(file_path)
        return "\n".join(para.text for para in doc.paragraphs)
    except Exception as e:
        raise RuntimeError(f"Error extracting text from DOCX: {e}")

def extract_from_image(file_path: str) -> str:
    try:
        image = Image.open(file_path)
        return pytesseract.image_to_string(image)
    except Exception as e:
        raise RuntimeError(f"Error extracting text from image: {e}")
