import psutil

####################################################################################################
## Function name :  ProcessDisplay   
## Description :    This Script is used to display all current running processes on our machine
## Author :         Girish Pradeep Patil
## Date :           10/02/2022
####################################################################################################

def ProcessDisplay():
    listprocess=[]

    for proc in psutil.process_iter():
        try:
            pinfo= proc.as_dict(attrs=['pid', 'name', 'username'])

            listprocess.append(pinfo)
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return listprocess

########################################################
## Starter function for ProcessDisplay function
######################################################## 
def main():
    print("Girish Patil : Display all running processes")
    print("Process Monitor")

    ret=ProcessDisplay()

    for element in ret:
        print(element)

if __name__=="__main__":
    main()