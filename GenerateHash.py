import hashlib
from termcolor import colored
username = "Mohammed@saad"
x = hashlib.sha256(username.encode("utf-8")).hexdigest()
    # haslib is library that is used for encryption and hashing algoritms in python
    # used sha256 to use algrithms of sha256
    # then we encoded string to utf-8 because this is funtion used by sha256
print("This is hash "+colored(x , 'yellow' ) + ' for ' + username)