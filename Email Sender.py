# Email Sender - Not finished yet

import smtplib
import ssl
from Read_functions import read_emails
import SendingFunctions

def main():
    stay = True
    answer = 1
    print("=========== Welcome in this email manager ===========")     
    while(stay):
        inputServer = input("Which server to want to connect to : ")
        address = input("What account do you want to use: ")
        password = input("What is the account's password : ")
        while(1):
            print("\n============== What do you want to do ================")
            print("1. Write a mail")
            print("2. Read inbox")
            print("3. Logout of the account")
            print("4. Quit app")
            answer = int(input("Your choice ? : "))
            if(answer == 1):
                SendingFunctions.writeMessage(inputServer, address, password)
            elif(answer == 2):
                read_emails(inputServer, address, password)
            elif(answer == 3):
                break
            elif(answer == 4):
                stay = False
                break


if __name__ == "__main__":
    main()