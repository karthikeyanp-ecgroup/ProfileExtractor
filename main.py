from email_reader import fetch_unread_emails
from file_processor import (
    extract_attachments, extract_text_from_pdf,
    extract_text_from_docx, extract_text_from_image
)
from resume_parser import parse_resume
from sheet_writer import write_to_sheet
import json
import os

def process():
    emails = fetch_unread_emails("imap.gmail.com", "karthisilicon@gmail.com", "njewlnpdbophbwuv")

    for msg in emails:
        files = extract_attachments(msg)

        for f in files:
            ext = f.split('.')[-1].lower()

            if ext == "pdf":
                text = extract_text_from_pdf(f)
            elif ext == "docx":
                text = extract_text_from_docx(f)
            elif ext in ["png", "jpg", "jpeg"]:
                text = extract_text_from_image(f)
            else:
                continue

            parsed = parse_resume(text)
            data = json.loads(parsed)

            write_to_sheet(data)

            print("Processed:", data["full_name"])

if __name__ == "__main__":
    process()
