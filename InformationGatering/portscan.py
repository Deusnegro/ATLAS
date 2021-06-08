from getpass import getuser
import sys
import time
import requests
from colorama import Fore
import getpass
import time
user = getpass.getuser()
def __start__():
    try:
        print(Fore.WHITE+"   /"+Fore.RED+"+"+Fore.BLUE+"\   "+Fore.WHITE+"Plase Enter IP / Domain\n")
        inp = input(Fore.RED+"  ┌──("+Fore.WHITE+"kali"+Fore.BLUE+"㉿"+Fore.WHITE+"kali"+Fore.RED+")"+Fore.WHITE+'-'+Fore.RED+"["+Fore.WHITE+"~/"+Fore.LIGHTMAGENTA_EX+"A"+Fore.LIGHTCYAN_EX+"T"+Fore.LIGHTRED_EX+"L"+Fore.YELLOW+"A"+Fore.BLUE+"S"+Fore.RED+"/"+Fore.WHITE+"M"+Fore.BLUE+"E"+Fore.GREEN+"N"+Fore.RED+"O"+Fore.YELLOW+"/"+Fore.LIGHTCYAN_EX+"I"+Fore.RED+"G"+Fore.LIGHTMAGENTA_EX+"/"+Fore.LIGHTCYAN_EX+"P"+Fore.LIGHTRED_EX+"O"+Fore.LIGHTMAGENTA_EX+"R"+Fore.LIGHTCYAN_EX+"T"+Fore.LIGHTRED_EX+"S"+Fore.YELLOW+"C"+Fore.BLUE+"A"+Fore.RED+"N"+Fore.RED+"]"+"""
  └─$ """+Fore.WHITE)
        result = requests.get('https://api.hackertarget.com/nmap/?q=' + inp).text
        out =input(" \n   Do You Want To Save The Output? yes/no  ")
        if out == "Yes" or out =="yes":
            map = "C:\\Users\\"+user+"\\Desktop\\"
            file=open(map+"Portscan - "+inp+".txt","w")
            file.write(str(result))
            time.sleep(0.5)
            print(Fore.CYAN+"\n   /"+Fore.RED+"+"+Fore.GREEN+"\   "+Fore.WHITE+"'Check Desktop'")
        elif out == "no" or out == "No":
            print("\n"+Fore.WHITE+result)
        try:
            time.sleep(0.5)
            input(Fore.RED+"   /"+Fore.MAGENTA+"M"+Fore.BLUE+"\   "+Fore.WHITE+"Back To Menu (Press Enter...) ")
        except:
            print("")
            sys.exit()  
        
    except:
        print("")
        sys.exit()
