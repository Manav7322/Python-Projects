import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html=Template(Path('Index.html').read_text())
email=EmailMessage()
email['from']='Manav Gupta'
email['to']='emailOfThePerson'
email['subject']='you won 100000 rupees!'
email.set_content(html.substitute({'name':'TinTin'}),'html')
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('yourEmailAccont@gmail.com','PasswordGeneratedByGoogleAccount')
    smtp.send_message(email)
    print('all good!')