import hashlib
from termcolor import colored
import pyfiglet
import argparse
import os

def Parsing():
    parse = argparse.ArgumentParser()
    parse.add_argument('-d ' , '--Dict' , dest="Dict" , help="Specify Dictionary you want to use it")
    parse.add_argument('-H' , '--hash' , dest="Hash" , help='Specify the Hashed Dict ')
    options = parse.parse_args()
    if not options.Dict :
        parse.error('Dictionary has not been specified ')
    elif not options.Hash :
        parse.error('Hashes has not been specified ')
    return options
os.system('cls')
text = pyfiglet.figlet_format(' HASH CRACK ')
text_color = colored(text , 'red' ,attrs=['bold'])
print(text_color)
options = Parsing()
with open (options.Dict , 'r') as i :
    common_pass = i.read().splitlines()

with open (options.Hash , 'r') as f :
    hashes = f.read().splitlines()

print('--------------------------------------------------------------------------')
print(colored(" Cracked Hashes  \t \t Their orginal hahses "  , 'green', attrs=['bold']))
print('--------------------------------------------------------------------------')

for passes in common_pass :
    hashing = hashlib.sha256(passes.encode('utf-8')).hexdigest()
    for AHash in hashes :
        if hashing == AHash :

            pases_color = colored(passes , 'cyan' , attrs=['bold'])
            hashing_color = colored(hashing , 'yellow' , attrs=['blink'])

            print('\t' + str(pases_color) + '\t\t' + str(hashing_color) + '\n')
