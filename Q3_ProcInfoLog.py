from sys import *
import psutil
import os

##################################################################################################
## Function name :  ProcessDisplay
## Input :          path
## Output :         Writes current process information into a log file  
## Description :    This script is to store current running process information into a log file
## Author :         Girish Pradeep Patil
## Date :           10/02/2022
##################################################################################################

def ProcessDisplay(path):
    listprocess=[]
    flag = os.path.isabs(path)
    if flag == False:
        path = os.path.abspath(path)

    exists = os.path.isdir(path)
    
    if exists:
        file_name='ProcessInfo.txt'             # If path exist then create a file as "ProcessInfo.txt"
        
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