#Main Variable
passwordlist = 'wordlist.txt'
#Import Libery
from hashlib import md5,sha1,sha256,sha384,sha512
from colorama import init,Fore
#Debug For Colors
init()
#Create Function For Hash Cracking
def hashcracking(hash,password):
    #Check Hash
    #Check Md5 Hash
    if hash == md5(password.encode()).hexdigest():
        print(Fore.GREEN+"Type :  MD5")
        print(Fore.GREEN+"Password Found: "+password)
        
    #Check Sha1 Hash
    elif hash == sha1(password.encode()).hexdigest():
        print(Fore.GREEN+"Type :  SHA1")
        print(Fore.GREEN+"Password Found: "+password)
       
    #Check Sha256 Hash
    elif hash == sha256(password.encode()).hexdigest():
         print(Fore.GREEN+"Type :  SHA256")
         print(Fore.GREEN+"Password Found: "+password)
       
    #Check Sha384 Hash
    elif hash == sha384(password.encode()).hexdigest():
        print(Fore.GREEN+"Type : SHA384")
        print(Fore.GREEN+"Password Found: "+password)
       
    #Check Sha512 Hash
    elif hash == sha512(password.encode()).hexdigest():
        print(Fore.GREEN+"Type :  SHA512")
        print(Fore.GREEN+"Password Found: "+password)
       
#Create Function For Read File And Enter Hash To hashcracking function
def read_and_check_hash(hash,passwordlist):
    #Open Password List
    with open(passwordlist,'r') as file:
        for line in file.readlines():
            #Run Hash Cracking Function
            hashcracking(hash,line.strip())
#Main Page and Main Command Line
def mainpage_and_commandline():
        while True:
                    
            print(Fore.LIGHTBLACK_EX+'>>>',end=' ')
            print(Fore.LIGHTMAGENTA_EX+'',end='')
            gethash =input('Enter Valid Hash:')
            read_and_check_hash(gethash,passwordlist)

mainpage_and_commandline()