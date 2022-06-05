# File containing all functions necessary to the sending of a message:
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import ssl
def writeMessage(inputServer, address, password):
    context = ssl.create_default_context()
    server = smtplib.SMTP_SSL("smtp." + inputServer, context=context)
    server.login(address, password)
    adressee = input("Who is the adressee ? : ")
    subject = input("What is the subject of the mail ? :")
    print("Your message : ")
    text = iter(input, '') # Get lines as input until an empty line.
    msgText = '\n'.join(text)
    nameList = address.split('.')
    name = [nameList[0][0].upper() + nameList[0][1:len(nameList[0])], 
    nameList[1].split('@')[0][0].upper() + nameList[1].split('@')[0][1:len(nameList[1]) - 1]]
    msg = message(name[0] + " " + name[1] + " <" + address + ">", adressee, subject=subject, text=msgText)
    server.sendmail(address, adressee, msg=msg.as_string())
    print("Email Sent !")
    server.quit()
    return

def message(address,addressee, subject="Without Subject", 
            text=""):
    # build message contents
    msg = MIMEMultipart()
    # Add Subject
    msg["From"] = address
    msg["To"] = addressee
    msg['Subject'] = subject
    # Add text contents
    msg.attach(MIMEText(text))
    return msg





if __name__ == "__main__":
    print("File containing all functions necessary to the sending of a message")