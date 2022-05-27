# Email Sender - Not finished yet

import smtplib
import ssl
import SendingFunctions

def main():
    stay = True
    answer = 1
    print("=========== Welcome in this email manager ===========")     
    while(stay):
        inputServer = input("Which server to want to connect to : ")
        address = input("What account do you want to use: ")
        password = input("What is the account's password : ")
        context = ssl.create_default_context()
        server = smtplib.SMTP_SSL(inputServer, context=context)
        server.login(address, password)
        while(1):
            print("\n============== What do you want to do ================")
            print("1. Write a mail")
            print("2. Read inbox")
            print("3. Logout of the account")
            print("4. Quit app")
            answer = int(input("Your choice ? : "))
            if(answer == 1):
                SendingFunctions.writeMessage(server, address)
            elif(answer == 2):
                readMessage()
            elif(answer == 3):
                break
            elif(answer == 4):
                stay = False
                break
        server.quit()


if __name__ == "__main__":
    main()