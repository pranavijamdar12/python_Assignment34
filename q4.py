import psutil
import os
import sys
import time
import smtplib
import mimetypes
from email.message import EmailMessage

# Create Log File
def ProcessLog(FolderName):

    Border = "-" * 50

    if not os.path.exists(FolderName):
        os.mkdir(FolderName)
        print("Directory created successfully.")

    timestamp = time.strftime("%Y_%m_%d_%H_%M_%S")

    LogFile = os.path.join(FolderName, "Marvellous_%s.log" % timestamp)

    fobj = open(LogFile, "w")

    fobj.write(Border + "\n")
    fobj.write("Marvellous Process Logger\n")
    fobj.write("Log Created At : " + timestamp + "\n")
    fobj.write(Border + "\n\n")

    for process in psutil.process_iter():

        try:
            info = process.as_dict(attrs=['pid', 'name', 'username'])

            fobj.write("Process Name : %s\n" % info['name'])
            fobj.write("PID          : %s\n" % info['pid'])
            fobj.write("Username     : %s\n" % info['username'])
            fobj.write(Border + "\n")

        except (psutil.NoSuchProcess,
                psutil.AccessDenied,
                psutil.ZombieProcess):
            pass

    fobj.close()

    print("Log File Created :", LogFile)

    return LogFile


# Send Mail with Attachment
def SendMail(Sender, Password, Receiver, Subject, Body, Attachment):

    msg = EmailMessage()

    msg["From"] = Sender
    msg["To"] = Receiver
    msg["Subject"] = Subject

    msg.set_content(Body)

    with open(Attachment, "rb") as f:
        data = f.read()

    FileType, Encoding = mimetypes.guess_type(Attachment)

    if FileType is None:
        MainType = "application"
        SubType = "octet-stream"
    else:
        MainType, SubType = FileType.split("/")

    msg.add_attachment(
        data,
        maintype=MainType,
        subtype=SubType,
        filename=os.path.basename(Attachment)
    )

    smtp = smtplib.SMTP_SSL("smtp.gmail.com", 465)

    smtp.login(Sender, Password.replace(" ", ""))

    smtp.send_message(msg)

    smtp.quit()

    print("Mail Sent Successfully")


def main():

    Border = "-" * 50

    print(Border)
    print("Marvellous Process Automation")
    print(Border)

    if len(sys.argv) != 3:

        print("Usage :")
        print("python ProcInfoLog.py FolderName ReceiverEmail")
        return

    FolderName = sys.argv[1]
    Receiver = sys.argv[2]

    Sender = input("Enter Sender Email : ")
    Password = input("Enter Gmail App Password : ")

    LogFile = ProcessLog(FolderName)

    Subject = "Process Log Report"

    Body = "Please find attached process log."

    SendMail(
        Sender,
        Password,
        Receiver,
        Subject,
        Body,
        LogFile
    )

    print(Border)
    print("Automation Completed Successfully")
    print(Border)


if __name__ == "__main__":
    main()
