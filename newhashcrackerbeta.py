#Main Variable
passwordlist = 'wordlist.txt'
#Import Libery
from hashlib import md5,sha1,sha256,sha384,sha512
from time import sleep
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
        return True
        
    #Check Sha1 Hash
    elif hash == sha1(password.encode()).hexdigest():
        print(Fore.GREEN+"Type :  SHA1")
        print(Fore.GREEN+"Password Found: "+password)
        return True
       
    #Check Sha256 Hash
    elif hash == sha256(password.encode()).hexdigest():
         print(Fore.GREEN+"Type :  SHA256")
         print(Fore.GREEN+"Password Found: "+password)
         return True
         
       
    #Check Sha384 Hash
    elif hash == sha384(password.encode()).hexdigest():
        print(Fore.GREEN+"Type : SHA384")
        print(Fore.GREEN+"Password Found: "+password)
        return True
       
    #Check Sha512 Hash
    elif hash == sha512(password.encode()).hexdigest():
        print(Fore.GREEN+"Type :  SHA512")
        print(Fore.GREEN+"Password Found: "+password)
        return True
        
    
        
       
#Create Function For Read File And Enter Hash To hashcracking function
def read_and_check_hash(hash,passwordlist):
    #Open Password List
    with open(passwordlist,'r') as file:
        for line in file.readlines():
            #Run Hash Cracking Function
            if hashcracking(hash,line.strip()):
                break
#Main Page and Main Command Line
def mainpage_and_commandline():
        while True:
                    
            text = Fore.GREEN+'''
┌─$HaskCracker @'''+Fore.RED+''' CommandLine
'''+Fore.LIGHTBLACK_EX+'''└──╼'''
            for c in text:
                print(c,end='')
                sleep(0.1)
            try:
                cm =input()
            except KeyboardInterrupt:
                print(Fore.GREEN+'\nGoodby.')
                exit()
            cm = cm.lower()
            if cm == 'help':
                print(Fore.RED+'\nfor crack hash:\n')
                
                print('\t'+Fore.MAGENTA+'>hash <yourhash>\n\n')
                print(Fore.RED+'for exit:\n')
                print('\t\t'+Fore.RED+'>exit\n')
                print(Fore.RESET+'')
            elif cm[:4] == 'hash' and len(cm) > 4:
               gethash = cm[5:]
               read_and_check_hash(gethash,passwordlist)
            elif cm == 'exit':
                exit()               
            else:
                print('Good if forget commmand type help')

                
                
            
           

mainpage_and_commandline()