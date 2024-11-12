import os
import smtplib
import ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Paramètres de connexion à Gmail
SMTP_SERVER = "smtp.gmail.com"
PORT = 465  # Port pour SSL direct (si vous souhaitez utiliser SSL)
EMAIL = os.environ.get("EMAIL")
PASSWORD = os.environ.get("PASSWORD")

subject = "My Second Email"
receiver_email = "akowakou251@gmail.com"

# Création du message de l'e-mail
message = MIMEMultipart()
message["From"] = EMAIL
message["To"] = receiver_email
message["Subject"] = subject

# Corps de l'e-mail en texte brut
body_text = "Hello there, I hope you are able to see my attached image."

# Ajouter le texte brut
message.attach(MIMEText(body_text, "plain"))

# Lire le contenu HTML à partir d'un fichier
html_filename = os.path.join(os.getcwd(), "email_content.html")

# Vérifier si le fichier HTML existe
if os.path.exists(html_filename):
    with open(html_filename, "r") as html_file:
        html_content = html_file.read()

    # Ajouter le contenu HTML à l'e-mail
    message.attach(MIMEText(html_content, "html"))
else:
    print(f"Le fichier {html_filename} n'a pas été trouvé.")

# Ajouter un fichier joint
filename = os.path.join(os.getcwd(), "images", "1.png")

# Vérifier si le fichier existe avant de continuer
if os.path.exists(filename):
    with open(filename, "rb") as attachment:
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())
        encoders.encode_base64(part)

        # Ajouter l'en-tête pour le fichier joint
        part.add_header(
            "Content-Disposition",
            f"attachment; filename={os.path.basename(filename)}",
        )

        message.attach(part)

# Convertir le message en chaîne de caractères
text = message.as_string()

# Création du contexte SSL et envoi de l'e-mail
context = ssl.create_default_context()
try:
    with smtplib.SMTP_SSL(SMTP_SERVER, PORT, context=context) as server:
        server.login(EMAIL, PASSWORD)
        server.sendmail(EMAIL, receiver_email, text)
        print("Email envoyé avec succès!")
except Exception as e:
    print(f"Erreur lors de l'envoi de l'email : {e}")
