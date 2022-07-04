import smtplib
from email.message import EmailMessage

email = EmailMessage()
email['from'] = 'Ayomide Richard'
email['to'] = 'gmail'
email['subject'] = 'You Won A Million Dollars'

email.set_content('I am a Python MF')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('email', 'password')
    smtp.send_message(email)
    print('Great')