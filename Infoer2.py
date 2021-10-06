import requests
import argparse
from termcolor import colored
import socket
import json
import os

def parser():
    parse = argparse.ArgumentParser()
    parse.add_argument("-u" ,"--url", dest="Url" , help= colored("Specify Url or Domain " ,'red' , attrs=["bold"]))

    options = parse.parse_args()
    if not options.Url :
        parse.error("You didn't specify URL or Domain")
    return options


# for executing Commands
os.system("cls")

parse = parser()

# Here we making A get request to HTTPS header and Specify them under one Variabale
req = requests.get("http://" + parse.Url)
# \n means on line
# and Here we printing value of Headers
print("\n" + ".......................................................")
print("\n" + str(req.headers))
print("\n" + "......................................................." + "\n")

# in socket module there is get host or Ipaddr by name which we use to get host from domain we give
hostIP = socket.gethostbyname(parse.Url)
print("\n" + colored("IP Addrress of " , 'magenta' , attrs=["bold"]) + str(parse.Url) + colored(" is " , 'magenta' , attrs=["bold"]) + str(hostIP) + '\n')


# to get Location from the domain we can rely on APi called ipinfo.io the gives us this kind of Service
# we put + "/jason to send Ip in Jason format
Location = requests.get("https://ipinfo.io/"+hostIP+"/json")
# now we have taken value from ipinfo.io and we print parts from it
resp_ = json.loads(Location.text)

# here we print Host and parts from jason response that in text
# Domian
print(colored("Domain : " , 'yellow' , attrs=["bold"]) + str(parse.Url))

# Location in IP
print(colored("HOST location in IP : " , 'cyan' , attrs=["bold"]) + resp_["loc"])

# Region
print(colored("Region : " , 'blue' , attrs=["bold"])  + resp_["region"])

# Country
print(colored("Country : " , 'cyan' , attrs=["bold"]) + resp_["country"])

# City
print(colored("City : " , 'red' , attrs=["bold"]) + str(resp_["city"]))