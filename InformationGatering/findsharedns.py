import requests
import sys
from colorama import Fore,init
import time
import getpass
init()
user = getpass.getuser()
def __start__():
    
    try:
        print(Fore.GREEN+"   /"+Fore.LIGHTCYAN_EX+"+"+Fore.BLUE+"\   "+Fore.WHITE+"Please Enter Domain/IP\n ")
        
        target = input(Fore.RED+" ┌──("+Fore.WHITE+"kali"+Fore.BLUE+"㉿"+Fore.WHITE+"kali"+Fore.RED+")"+Fore.WHITE+'-'+Fore.RED+"["+Fore.WHITE+"~/"+Fore.LIGHTMAGENTA_EX+"A"+Fore.LIGHTCYAN_EX+"T"+Fore.LIGHTRED_EX+"L"+Fore.YELLOW+"A"+Fore.BLUE+"S"+Fore.RED+"/"+Fore.WHITE+"M"+Fore.BLUE+"E"+Fore.GREEN+"N"+Fore.RED+"O"+Fore.YELLOW+"/"+Fore.LIGHTCYAN_EX+"I"+Fore.RED+"G"+Fore.LIGHTMAGENTA_EX+"/"+Fore.LIGHTCYAN_EX+"F"+Fore.LIGHTRED_EX+"S"+Fore.YELLOW+"D"+Fore.RED+"]"+"""
 └─$ """+Fore.WHITE)
        req = requests.get("https://api.hackertarget.com/httpheaders/?q="+target).text
        out =input(" \n   Do You Want To Save The Output? yes/no  ")
        if out == "Yes" or out =="yes":
            map = "C:\\Users\\"+user+"\\Desktop\\"
            file=open(map+"FindShereDNS - "+target+".txt","w")
            file.write(str(req))
            time.sleep(0.5)
            print(Fore.CYAN+"\n   /"+Fore.RED+"+"+Fore.GREEN+"\   "+Fore.WHITE+"'Check Desktop'\n")
        elif out == "no" or out == "No":
            print("\n"+Fore.WHITE+req)
        try:
            time.sleep(0.5)
            input(Fore.YELLOW+"   /"+Fore.LIGHTRED_EX+"M"+Fore.WHITE+"\   "+Fore.WHITE+"Back To Menu (Press Enter...) ")
        except:
             print("")
             sys.exit()

    except:
        print("")
        sys.exit()


