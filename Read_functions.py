import imaplib
import email
from ssl import create_default_context


def read_emails(inputServer, address, password):
    server = imaplib.IMAP4_SSL("imap." + inputServer)
    server.login(address, password)
    server.select("inbox")
    _, mails_indexes = server.search(None, "ALL") # Return a list of all indexes of all emails
    for index in mails_indexes[0].split():
        print("===========================================")
        mail = get_mail(server, index)
        print_mail(mail)
        print("\n============== What do you want to do ================")
        print("1. Move mail")
        print("2. Delete mail")
        print("3. Mark")
        print("4: Delete SPAM")
        print("5. Pass")
        print("6. Quit app")
        answer = int(input("Your choice ? : "))
        if(answer == 1):
            # TODO Create a function that takes dstFolder and srcFolder and moves mails
            pass
        elif(answer == 2):
            print("Deleting {}".format(mail["subject"]))
            server.store(mail, "+FLAGS", "\\Deleted")
        elif(answer == 3):
            server.store(mail, "+FLAGS", "\\Flagged")
        elif(answer == 4):
            # TODO Work on a file searching with all spam addresses to delete all spam mails 
            pass
        elif(answer == 5):
            pass
        elif(answer == 6):
            server.expunge()
            break
    server.close()
    server.logout()
    return 0

def get_mail(server, index):
    _, mail_data = server.fetch(index, "(RFC822)") # get all the emails including the meta-data
    _, mail_bytes = mail_data[0] # takes only the important part for reader
    mail_message = email.message_from_bytes(mail_bytes) # convert it into a string
    return mail_message

def print_mail(mail_message):
    for header in ["subject", "to", "from", "date"]:
        print("{} : {}".format(header, mail_message[header]))
    for part in mail_message.walk():
        if(part.get_content_type() == ("text/plain" or "text.html")):
            body = part.get_payload(decode=True)
            print(body.decode())
    
if __name__ == "__main__":
    print("All functions necessary to read inbox")