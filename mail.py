from config import settings
import smtplib, ssl

def email(reply_address, message):
    port = 465  # For SSL
    smtp_server = "smtp.gmail.com"
    sender_email = "maschadeveloper@gmail.com"  # Enter your address
    receiver_email = "maschavandermarel@gmail.com"
    password = settings.email_pwd
    mail =f"""\
reply-to: {reply_address}
subject: {reply_address} seeks contact

{message}"""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, mail)

