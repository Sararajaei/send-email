import smtplib

HOST = 'smtp.gmail.com'
USER = 'sararj9894@gmail.com'
PASSWORD = 'ziawbzfzyyztkemj'
PORT = 465


def send_email(contact, body):
    with smtplib.SMTP_SSL(HOST, PORT) as server:
        server.login(USER, PASSWORD)
        server.sendmail(USER, contact, body)
