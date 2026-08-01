import psutil
import sys
import os
import time
def ProcessLog(FolderName):
    Border = "-"*50
    if(os.path.exists(FolderName)==False):
        os.mkdir(FolderName)
        print("Directory created Sucessfully")
    timestamp = time.strftime("%Y_%m_%d_%H_%M_%S")
    FileName = os.path.join(FolderName,"Marvellous_%s.log"%timestamp)
    fobj = open(FileName,"w")
    fobj.write(Border +"\n")
    fobj.write("Marvellous Process Log\n")
    fobj.write("Log Created At:"+timestamp+"\n")
    fobj.write(Border + "\n\n")

    for process in psutil.process_iter():
        try:
            ProcessInfo = process.as_dict(attrs=['pid','username','name'])
            fobj.write("Process Name: %s\n"%ProcessInfo['name'])
            fobj.write("UserName: %s\n"%ProcessInfo['username'])
            fobj.write("PID: %s\n"%ProcessInfo['pid'])
            fobj.write(Border + "\n")
        except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
            pass
    fobj.close()
    print("Log File Created Sucessfully.")
    print("Log File:",FileName)

def main():
    Border = "-"*50
    print(Border)
    print("------------------Marvellous process Logger-------------")
    print(Border)
    if(len(sys.argv)==2):
        if(sys.argv[1]=="--h" or sys.argv[1]=="--H"):
            print("This Automation Script Created a Log file")
            print("contaning information of all running process")
        elif(sys.argv[1]=="--u" or sys.argv[1]=="--U"):
            print("Usage")
            print("python",sys.argv[0],"DirectoryName")
        else:
            ProcessLog(sys.argv[1])
    else:
        print("Invalid Number OF arugments.")
        print("use --h and --u for help")
    print(Border)
    print("Thank you for using Marvellous Automation")
    print(Border)

if __name__ == "__main__":
    main()
