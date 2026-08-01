    #design automation script which display information process as its name,PID,username
import psutil
import sys

def ProcessDisplay():
    Border = "-"*50

    print(Border)
    print("Information of Running Process")
    print(Border)

    for process in psutil.process_iter():
        try:
            ProcessInfo = process.as_dict(attrs=['pid','name','username'])
            print("Process Name:",ProcessInfo['name'])
            print("PID:",ProcessInfo['pid'])
            print("username:",ProcessInfo['username'])

        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass

        
def main():
    Border = "-"*50
    print(Border)
    print("-------------Marvellous Process Automation---------------")
    print(Border)

    if(len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This Automation Script Display Informatiom")
            print("of all running process.")
            print("It Display Process Name,PID and username.")
        elif(sys.argv[1]=="--u" or sys.argv[1]=="U"):
            print("Usage")
            print("Python",sys.argv[0])
        else:
            print("unable process as invalid arguments.")
            print("use --h and --u for help.")
    elif(len(sys.argv)==1):
        ProcessDisplay()
    else:
        print("Invalid Number of Argumets")
        print("use --h or --u for help")
    print(Border)
    print("Thankuu for using Marvellous Automation")
    print(Border)
if __name__ == "__main__":
    main()
