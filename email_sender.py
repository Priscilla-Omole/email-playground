import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

load_dotenv()

EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_APP_PASSWORD')

email = EmailMessage()
email['from'] = 'John Doe'
email['to'] = 'xyxy@gmail.com'
email['subject'] = 'You won a 1,00000 dollars!'

email.set_content('I am a python master!')

with smtplib.SMTP_SSL(host='smtp.gmail.com', port=465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(email)
    print('all good boss')