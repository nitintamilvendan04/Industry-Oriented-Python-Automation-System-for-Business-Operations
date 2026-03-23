import smtplib
from email.mime.text import MIMEText
from config import EMAIL, PASSWORD, SMTP_SERVER, SMTP_PORT
from logger import log_info, log_error

def send_email(receiver_email, subject, body):
    try:
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = EMAIL
        msg["To"] = receiver_email

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL, PASSWORD)
        server.sendmail(EMAIL, receiver_email, msg.as_string())
        server.quit()

        log_info("Email sent successfully")

    except Exception as e:
        log_error(f"Error sending email: {e}")