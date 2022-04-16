from hashlib import  md5,sha1,sha256,sha384,sha512
from colorama import init,Fore

init()

string = input('Enter Text For Encrypt:')
string = string.encode()
print(Fore.LIGHTBLACK_EX)
print('MD5:',md5(string).hexdigest())
print('SHA1:',sha1(string).hexdigest())
print(Fore.RED)
print('SHA256:',sha256(string).hexdigest())
print('SHA384:',sha384(string).hexdigest())
print(Fore.GREEN)
print('SHA512:',sha512(string).hexdigest())
print(Fore.RESET+'This Is Your Hash ')
