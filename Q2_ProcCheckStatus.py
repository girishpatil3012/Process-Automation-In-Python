import psutil
from sys import *

######################################################################################################################
## Function name :  CheckProcessStatus
## Input :          processname  
## Description :    This Script is used to check and display whether the specific process is running/active or not
## Author :         Girish Pradeep Patil
## Date :           10/02/2022
#####################################################################################################################

def CheckProcessStatus(processname):
    for proc in psutil.process_iter():
        try:
            if processname.lower() in proc.name().lower():
                return True
        except(psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return False

########################################################
## Starter function for CheckProcessStatus function
######################################################## 
def main():
    print("---- Girish Patil : Automation Script -----")
    print("Application name: ",argv[0])

    if (len(argv)!=2):
        print("Error : invalid number of arguements")
        exit()

    if argv[1]=="-h" or argv[1]=="-H":
        print("This script is to display whether the process is running or not")
        exit()

    if argv[1]=="-u" or argv[1]=="-U":
        print("Usage  : Application Name Currently Running Process Information")
        exit()

    try:
        if CheckProcessStatus(argv[1]):
            print("Yes process is running")
        else:
            print("Process not found as running")
    
    except ValueError:
        print("Error : Invalid input of data type")

    except Exception as E:
        print("Error : Inavlid Input",E)


if __name__=="__main__":
    main()