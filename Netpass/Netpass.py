import subprocess
import os
import pyfiglet
import re
from termcolor import colored


# Name part 
os.system('cls')
text = pyfiglet.figlet_format('NetPass')
text_color = colored(text , 'yellow' , attrs=['bold'])
print(text_color)
# Using regular expression part for getting user Profiles Part
command = subprocess.check_output("netsh wlan show profiles")
profile_names = (re.findall("All User Profile     : (.*)\r", command))

# Main Head Party 
print(colored('----------------------------------------------------------------' , 'green' , attrs=['bold']))
print(colored('SSID\t\tSecurity Avability\t\tPassword' , 'blue' , attrs=['bold']))
print(colored('----------------------------------------------------------------' , 'green' , attrs=['bold']))


# This is mutipile loop which will ittorate over those lists


# using regular expression and commands to get key state and content 
def prx(profile):
    for x  in profile:
        try :
            commandTwo = subprocess.check_output('netsh wlan show profiles '+ x +' key=clear')
            security_ava = (re.findall(" Security key           :(.*)\r", commandTwo))
            key_content = re.findall("Key Content            :(.*)\r", commandTwo)
            print(str(x) + '\t\t' + colored(str(security_ava) , 'red' , attrs=['bold']) + '\t\t' + str(key_content))
        except subprocess.CalledProcessError:
            pass
prx(profile_names)
