from datetime import datetime
import imaplib
import email
import os
from email.header import decode_header

EMAIL = "karthisilicon@gmail.com"
APP_PASSWORD = "opshxvflgjvgsork"
ATTACHMENT_DIR = "profiles"

mail = imaplib.IMAP4_SSL("imap.gmail.com")
mail.login(EMAIL, APP_PASSWORD)

mail.select("inbox")
today = datetime.today().strftime("%d-%b-%Y")

# Search unread mails received since today
status, messages = mail.search(None, '(UNSEEN SINCE "{}")'.format(today))

email_ids = messages[0].split()

print("Unread emails today:", email_ids)
os.makedirs(ATTACHMENT_DIR, exist_ok=True)
for eid in email_ids:
    # Fetch full email
    status, msg_data = mail.fetch(eid, "(RFC822)")
    msg = email.message_from_bytes(msg_data[0][1])

    # Decode subject
    subject, encoding = decode_header(msg["Subject"])[0]
    if isinstance(subject, bytes):
        subject = subject.decode(encoding or "utf-8")

    print(f"\n📧 Subject: {subject}")

    # Process email parts
    for part in msg.walk():
        # Skip plain text and HTML
        if part.get_content_maintype() == "multipart":
            continue

        # If it has an attachment
        if part.get("Content-Disposition"):
            filename = part.get_filename()

            if filename:
                # Decode filename if needed
                filename, encoding = decode_header(filename)[0]
                if isinstance(filename, bytes):
                    filename = filename.decode(encoding or "utf-8")

                # Save attachment
                filepath = os.path.join(ATTACHMENT_DIR, filename)
                with open(filepath, "wb") as f:
                    f.write(part.get_payload(decode=True))

                print(f"📎 Saved attachment: {filepath}")

print("\nDone!")