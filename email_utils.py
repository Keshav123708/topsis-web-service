import smtplib
import os
from email.message import EmailMessage


def send_email(receiver_email, attachment_path):
    # Get credentials from environment variables
    EMAIL_ADDRESS = os.environ.get("EMAIL_ADDRESS")
    EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")

    if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
        raise Exception("Email credentials not set in environment variables")

    # Create email
    msg = EmailMessage()
    msg["Subject"] = "TOPSIS Result File"
    msg["From"] = EMAIL_ADDRESS
    msg["To"] = receiver_email
    msg.set_content(
        "Hello,\n\nPlease find attached the TOPSIS result file.\n\nRegards\nTOPSIS Web Service"
    )

    # Attach CSV
    with open(attachment_path, "rb") as f:
        msg.add_attachment(
            f.read(),
            maintype="application",
            subtype="octet-stream",
            filename="result.csv"
        )

    # Send email using Gmail SMTP
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        server.send_message(msg)
