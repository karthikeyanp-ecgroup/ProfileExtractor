import imaplib
import email
from datetime import datetime
from email.header import decode_header

def fetch_unread_emails(imap_host, email_user, email_pass):
    mail = imaplib.IMAP4_SSL(imap_host)
    mail.login(email_user, email_pass)
    mail.select("inbox")
    today = datetime.today().strftime("%d-%b-%Y")

    status, messages = mail.search(None, '(UNSEEN SINCE "{}")'.format(today))
    email_ids = messages[0].split()

    mails = []
    for e_id in email_ids:
        status, msg_data = mail.fetch(e_id, "(RFC822)")
        msg = email.message_from_bytes(msg_data[0][1])
        mails.append(msg)

    return mails
