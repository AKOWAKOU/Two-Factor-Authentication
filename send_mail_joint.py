import os
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

SMTP_SERVER = "smtp.gmail.com"
PORT = 465  
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

subject = "My Second Email"
body = "Hello there, I hope you are able to see my attached image."
receiver_email = "akowakou251@gmail.com"

message = MIMEMultipart()
message["From"] = EMAIL
message["To"] = receiver_email
message["Subject"] = subject

message.attach(MIMEText(body, "plain"))

filename = os.path.join(os.getcwd(), "images", "1.png")

if not os.path.exists(filename):
    print(f"Le fichier {filename} n'existe pas.")
else:
    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)

        part.add_header(
            "Content-Disposition",
            f"attachment; filename={os.path.basename(filename)}",
        )

        message.attach(part)

    text = message.as_string()

    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL(SMTP_SERVER, PORT, context=context) as server:
            server.login(EMAIL, PASSWORD)
            server.sendmail(EMAIL, receiver_email, text)
            print("Email envoyé avec succès!")
    except Exception as e:
        print(f"Erreur lors de l'envoi de l'email : {e}")
