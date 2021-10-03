import subprocess
import os
import re
from termcolor import colored
# Name part 
os.system('cls')
#text = pyfiglet.figlet_format('NetPass')
#text_color = colored(text , 'yellow' , attrs=['bold'])
print(colored(""" _   _      _   ____
| \ | | ___| |_|  _ \ __ _ ___ ___
|  \| |/ _ \ __| |_) / _` / __/ __|
| |\  |  __/ |_|  __/ (_| \__ \____ 
|_| \_|\___|\__|_|   \__,_|___/___/  """ , "cyan" , attrs=["bold"]) + '\n')

# Using regular expression part for getting user Profiles Part
command = subprocess.check_output("netsh wlan show profiles")
profile_names = (re.findall("All User Profile     : (.*)\r", str(command)
                            ))

# Main Head Party
print(colored('----------------------------------------------------------------' , "red" , attrs=["bold"]))
print (colored('SSID\t\tSecurity Avability\t\tPassword' , "yellow" , attrs=["bold"]))
print(colored('----------------------------------------------------------------' , "red" , attrs=["bold"]))


# This is mutipile loop which will ittorate over those lists


# using regular expression and commands to get key state and content 
def prx(profile):
    for x in profile:
        try :
            commandTwo = subprocess.check_output('netsh wlan show profiles '+ '"{}"'.format(x) +' key=clear')
            security_ava = (re.findall(" Security key           :(.*)\r", commandTwo))
            key_content = re.findall("Key Content            :(.*)\r", commandTwo)
            print(str(x) + '\t\t' + str(security_ava) + '\t\t' + str(key_content))
        except subprocess.CalledProcessError:
            pass
prx(profile_names)
