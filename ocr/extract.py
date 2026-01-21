import pdfplumber
import pytesseract
from PIL import Image
import requests
from bs4 import BeautifulSoup
from pdf2image import convert_from_path
import os
import tempfile

def extract_from_pdf(path):
    text = ""

    # Try normal text extraction first
    try:
        with pdfplumber.open(path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text
    except:
        pass

    # If text is too small, use OCR fallback

    if len(text.strip()) < 50:
        print("⚠️ Scanned PDF detected. Running OCR...")

        images = convert_from_path(path)
        for img in images:
            text += pytesseract.image_to_string(img)

    return text


def extract_text_from_pdf(path):
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def extract_from_image(path):
    img = Image.open(path)
    return pytesseract.image_to_string(img)

def extract_from_url(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    return soup.get_text()
