import requests
import sys
from colorama import Fore,init
import time
import getpass
user = getpass.getuser()
init()
def __start__():
    
    try:
        print(Fore.GREEN+"   /"+Fore.YELLOW+"+"+Fore.WHITE+"\   "+Fore.WHITE+"Please Enter Domain \n")
        target = input(Fore.RED+"  ┌──("+Fore.WHITE+"kali"+Fore.BLUE+"㉿"+Fore.WHITE+"kali"+Fore.RED+")"+Fore.WHITE+'-'+Fore.RED+"["+Fore.WHITE+"~/"+Fore.LIGHTMAGENTA_EX+"A"+Fore.LIGHTCYAN_EX+"T"+Fore.LIGHTRED_EX+"L"+Fore.YELLOW+"A"+Fore.BLUE+"S"+Fore.RED+"/"+Fore.WHITE+"M"+Fore.BLUE+"E"+Fore.GREEN+"N"+Fore.RED+"O"+Fore.YELLOW+"/"+Fore.LIGHTCYAN_EX+"I"+Fore.RED+"G"+Fore.LIGHTMAGENTA_EX+"/"+Fore.LIGHTCYAN_EX+"W"+Fore.LIGHTRED_EX+"H"+Fore.LIGHTMAGENTA_EX+"O"+Fore.LIGHTCYAN_EX+"I"+Fore.LIGHTRED_EX+"S"+Fore.RED+"]"+"""
  └─$ """+Fore.WHITE)
        print("")
        req = requests.get("https://api.hackertarget.com/whois/?q="+target).text
        out =input(" \n   Do You Want To Save The Output? yes/no  ")
        if out == "Yes" or out =="yes":
            map = "C:\\Users\\"+user+"\\Desktop\\"
            file=open(map+"Whois - "+target+".txt","w")
            file.write(str(req))
            time.sleep(0.5)
            print(Fore.CYAN+"\n   /"+Fore.RED+"+"+Fore.GREEN+"\   "+Fore.WHITE+"'Check Desktop'\n")
        elif out == "no" or out == "No":
            print("\n"+Fore.WHITE+req)

        try:
            input(Fore.RED+"   /"+Fore.LIGHTBLUE_EX+"M"+Fore.BLUE+"\   "+Fore.WHITE+"Back To Menu (Press Enter...) ")
        except:
             print("")
             sys.exit()

    except:
        print("")
        sys.exit()


