from sys import argv
from hashlib import md5,sha1,sha256,sha384
args = argv
hashs = args[1]
passwordlist = args[2]
def hash_func(password,hashed_password):
    if md5(password.encode()).hexdigest() == hashed_password:
        print(password)
        exit()
    elif sha1(password.encode()).hexdigest() == hashed_password:
        print(password)
        exit()
    elif sha256(password.encode()).hexdigest() == hashed_password:
        print(password)
        exit()
    elif sha384(password.encode()).hexdigest() == hashed_password:
        print(password)
        exit()

def readfile(passwordlist):
    with open(passwordlist,'r') as file:
        for line in file.readlines():
            hash_func(line.strip(),hashs)
readfile(passwordlist)
                