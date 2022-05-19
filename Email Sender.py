# Email Sender - Not finished yet

import smtplib
import ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

inputServer = input("What is the server to use : ")
adress = input("What is the account to use : ")
password = input("What is the account's password : ")
adressee = input("Who is the adressee : ")
msgText = input("What is the message : ")

def message(subject="Notification", 
            text=""):
    
    # build message contents
    msg = MIMEMultipart()
      
    # Add Subject
    msg["From"] = adress
    msg["To"] = adressee
    msg['Subject'] = subject  
      
    # Add text contents
    msg.attach(MIMEText(text))
    return msg

context = ssl.create_default_context()
server = smtplib.SMTP_SSL(inputServer, context=context)
server.login(adress, password)

msg = message(text=msgText)
server.sendmail(adress, adressee, msg=msg.as_string())
server.quit()