import smtplib

def send_notification(email, name):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login("your-email@gmail.com", "app-password")

    message = f"New candidate added: {name}"
    server.sendmail("your-email@gmail.com", email, message)
    server.quit()
