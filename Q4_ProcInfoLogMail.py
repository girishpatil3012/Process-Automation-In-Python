from sys import *
import psutil
import os
import smtplib
import mimetypes
from email.message import EmailMessage

############################################################################################################################
## Function name :  ProcessDisplay
## Input :          path
## Output :         Writes current process information into a log file and mails that file 
## Description :    This script is to store current running process information into a log file and mails to given mailid
## Author :         Girish Pradeep Patil
## Date :           10/02/2022
############################################################################################################################

def ProcessDisplay(path):
    file_name='ProcessInfo.txt'
    listprocess=[]

    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)

    message = EmailMessage()
    sender = "senders_mail_id"
    recipient = "reciever_mail_id"
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = 'Running Processes Information in Log file'
    body = """Hello
    Log file is attached in this mail!!!"""
    message.set_content(body)
    mime_type, _ = mimetypes.guess_type('ProcessInfo.txt')
    mime_type, mime_subtype = mime_type.split('/')
    with open(os.path.join(path,file_name),'rb') as file:
        message.add_attachment(file.read(),
        maintype=mime_type,
        subtype=mime_subtype,
        filename='ProcessInfo.txt')
    print(message)
    mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
    mail_server.set_debuglevel(1)
    mail_server.login("senders_mail_id", 'senders_mail_id_password')
    mail_server.send_message(message)
    mail_server.quit()
    
    if exists:
        #file_name='ProcessInfo.txt'
        
        for foldername, subfolder, filname in os.walk(path):
            print("Log File Successfully Created in : "+foldername)

            for subf in subfolder:
                print("Sub folder of "+foldername+"is :"+subf)

            for filen in filname:
                print("File inside "+foldername+"is : "+filen)
                
            print('')
    else:
        print("Invalid Path")

    for proc in psutil.process_iter():

        try:
            pinfo= proc.as_dict(attrs=['pid', 'name', 'username'])

            listprocess.append(pinfo)
            with open(os.path.join(path,file_name),'w') as filehandle:
                for listitem in listprocess:
                    filehandle.write('%s\n' % listitem)
                    continue
            

        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
        
    return listprocess  

########################################################
## Starter function for ProcessDisplay function
########################################################                 
def main():
    print("----Girish Patil : Automation Script-----")
    print("Application name: ",argv[0])

    if (len(argv)!=2):
        print("Error : invalid number of arguements")
        exit()

    if argv[1]=="-h" or argv[1]=="-H":
        print("This script is to store current running process information into a log file")
        exit()

    if argv[1]=="-u" or argv[1]=="-U":
        print("Usage  : Application Name Currently Running Process Information")
        exit()

    try:
        ProcessDisplay(argv[1])

    except ValueError:
        print("Error : Invalid input of data type")

    except Exception as E:
        print("Error : Inavlid Input",E) 

if __name__=="__main__":
    main()