import builtwith
from colorama import Fore,init
import sys
import getpass
user=getpass.getuser()
init()
def __start__():

 try:
    print(Fore.BLUE+"   /"+Fore.YELLOW+"+"+Fore.MAGENTA+"\   "+Fore.WHITE+"Plase Enter Domain\n")
    target = input(Fore.RED+"  ┌──("+Fore.WHITE+"kali"+Fore.BLUE+"㉿"+Fore.WHITE+"kali"+Fore.RED+")"+Fore.WHITE+'-'+Fore.RED+"["+Fore.WHITE+"~/"+Fore.LIGHTMAGENTA_EX+"A"+Fore.LIGHTCYAN_EX+"T"+Fore.LIGHTRED_EX+"L"+Fore.YELLOW+"A"+Fore.BLUE+"S"+Fore.RED+"/"+Fore.WHITE+"M"+Fore.BLUE+"E"+Fore.GREEN+"N"+Fore.RED+"O"+Fore.YELLOW+"/"+Fore.LIGHTCYAN_EX+"I"+Fore.RED+"G"+Fore.LIGHTMAGENTA_EX+"/"+Fore.LIGHTCYAN_EX+"C"+Fore.LIGHTRED_EX+"M"+Fore.YELLOW+"S"+Fore.BLUE+"D"+Fore.RED+"E"+Fore.WHITE+"T"+Fore.BLUE+"E"+Fore.GREEN+"C"+Fore.MAGENTA+"T"+Fore.RED+"]"+"""
  └─$ """+Fore.WHITE)


    if "http://" in target:
        pass
    elif not "http://" in target:
        target = 'http://'+target

    info = builtwith.parse(target)


    for name in info:
        value = ''
        for val in info[str(name)]:
            name = name.replace('-',' ')
            name = name.title()
            value += str(val) 
            res =  name+': '+value
        print(Fore.WHITE+res)
    try:
         input(Fore.BLUE+"\n   /"+Fore.YELLOW+"M"+Fore.MAGENTA+"\   "+Fore.WHITE+"Back To Menu (Press Enter...) ")
    except:
         print("")
         sys.exit()


 except:
         print("")
         sys.exit()







