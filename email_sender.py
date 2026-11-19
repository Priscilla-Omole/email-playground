import smtplib
import os
from email.message import EmailMessage
from dotenv import load_dotenv
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())

load_dotenv()

EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_APP_PASSWORD')

email = EmailMessage()
email['from'] = 'John Doe'
email['to'] = 'xysdnd@gmail.com'
email['subject'] = 'You won a 1,00000 dollars!'

email.set_content(html.substitute({'name':'Tintin'}), 'html')

with smtplib.SMTP_SSL(host='smtp.gmail.com', port=465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(email)
    print('all good boss')