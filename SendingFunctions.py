# File containing all functions necessary to the sending of a message:

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def writeMessage(server, address):
    name = input("From whom this email is ? : ")
    adressee = input("Who is the adressee : ")
    text = iter(input, '') # Get lines as input until an empty line.
    msgText = '\n'.join(text)
    msg = message(address, adressee, subject="Mail Test", text=msgText)
    server.sendmail(address, adressee, msg=msg.as_string())
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