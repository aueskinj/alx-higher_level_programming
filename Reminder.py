import smtplib
import os 
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

EMAIL_ADDRESS = "aueskinj@gmail.com"
EMAIL_PASSWORD = "tvju lamd cgtj ffuz"

SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587

def send_email(recipient_email, subject, body):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = recipient_email
        msg['Subject'] = subject

        msg.attach(MIMEText(body, 'plain'))
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, recipient_email, msg.as_string())
        
        print(f"Email sent to {recipient_email}")
    except Exception as e:
        print(f"Failed to send email: {e}")

if __name__ == "__main__":
    recipient_email = "aueskinj@gmail.com"
    subject = "This is the subject"
    body = "This is the body of the email."

    send_email(recipient_email, subject, body)
