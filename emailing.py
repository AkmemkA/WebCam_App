import os
import smtplib
import ssl


def send_email(file):
    host = "smtp.gmail.com"
    port = 465
    user_name = "Akhmedka1993@gmail.com"
    password = os.getenv("PASSWORD")
    recipient = "kodi199312@gmail.com"
    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(user_name, password)
        server.sendmail(user_name, recipient, file)
