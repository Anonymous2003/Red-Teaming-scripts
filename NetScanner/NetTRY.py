import scapy.all as scapy
import argparse
import pyfiglet
import os
from termcolor import colored
def parser():
    parse = argparse.ArgumentParser()
    parse.add_argument('-t' , '--target' , dest='target' , help='specify IP range ')
    options = parse.parse_args()
    if not options.target:
        parse.error(' Target has not been specified ')
    return options

def scan(ip):
    print('---------------------------------------')
    print('Mac Address \t\t Vendor \t IP ')
    print('---------------------------------------')
    scapy.arping(ip)

os.system('cls')
options = parser()
scan(options.target)

