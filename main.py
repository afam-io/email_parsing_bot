import os
from dotenv import load_dotenv
import smtplib

load_dotenv()

EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("afam.dev.1@gmail.com", EMAIL_PASSWORD)
