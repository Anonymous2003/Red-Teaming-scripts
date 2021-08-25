import hashlib
import subprocess
import re
import argparse
import os
from termcolor import colored 
def parser():
    parse = argparse.ArgumentParser()
    parse.add_argument("-P"  , '--path' , dest="path" , help="Specify The Path ")
    #parse.add_argument("-A"  , '--Algorithms' , dest="Algo" , help="Specify The Path ")
    options = parse.parse_args()

    if not options.path :
        parse.error(" Path has not been specified ")
    #if not options.Algo :
      #  parse.error(" Algorithm Type has not been specified ")
    return options

def AHASH(bfile) :
    hasher = hashlib.sha256()
    with open(bfile , 'rb') as afile:
        buf = afile.read()
        hasher.update(buf)
    print(colored("hash Vaue : " , "red") + str(hasher.hexdigest()))
os.system("cls")
options = parser()

AHASH(options.path)
