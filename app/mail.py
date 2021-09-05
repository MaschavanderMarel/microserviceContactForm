from config import *
import smtplib, ssl

def send_email(reply_address: str, message: str):
    
    port =  465 if smtp_port == EMPTY_VALUE else smtp_port # Default: SMTP over SSL
    email_recipient = email_from if email_to == EMPTY_VALUE else email_to # Default: send to self
    mail =f"""\
reply-to: {reply_address}
subject: {reply_address} seeks contact
to: {email_recipient}

{message}"""

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
        server.ehlo_or_helo_if_needed()
        server.login(email_from, email_pwd)
        server.sendmail(email_from, email_recipient, mail)

