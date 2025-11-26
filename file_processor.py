import os
import pdfplumber
from docx import Document
from PIL import Image
import pytesseract

def extract_attachments(msg, download_folder="profiles"):
    files = []
    for part in msg.walk():
        if part.get_content_maintype() == 'multipart':
            continue
        if part.get('Content-Disposition') is None:
            continue

        filename = part.get_filename()
        if filename:
            filepath = os.path.join(download_folder, filename)
            with open(filepath, "wb") as f:
                f.write(part.get_payload(decode=True))
            files.append(filepath)

    return files


def extract_text_from_pdf(path):
    text = ""
    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + "\n"
    return text


def extract_text_from_docx(path):
    doc = Document(path)
    return "\n".join([p.text for p in doc.paragraphs])


def extract_text_from_image(path):
    img = Image.open(path)
    return pytesseract.image_to_string(img)
