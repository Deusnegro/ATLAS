import requests
import sys
from colorama import Fore,init
import time
import getpass
user = getpass.getuser()
init()
def __start__():
    
    try:
        print(Fore.BLUE+"   /"+Fore.LIGHTRED_EX+"+"+Fore.MAGENTA+"\   "+Fore.WHITE+"Plase Enter IP/Domain\n")
        target = input(Fore.RED+"  ┌──("+Fore.WHITE+"kali"+Fore.BLUE+"㉿"+Fore.WHITE+"kali"+Fore.RED+")"+Fore.WHITE+'-'+Fore.RED+"["+Fore.WHITE+"~/"+Fore.LIGHTMAGENTA_EX+"A"+Fore.LIGHTCYAN_EX+"T"+Fore.LIGHTRED_EX+"L"+Fore.YELLOW+"A"+Fore.BLUE+"S"+Fore.RED+"/"+Fore.WHITE+"M"+Fore.BLUE+"E"+Fore.GREEN+"N"+Fore.RED+"O"+Fore.YELLOW+"/"+Fore.LIGHTCYAN_EX+"I"+Fore.RED+"G"+Fore.LIGHTMAGENTA_EX+"/"+Fore.LIGHTCYAN_EX+"D"+Fore.LIGHTRED_EX+"N"+Fore.YELLOW+"S"+Fore.BLUE+"L"+Fore.RED+"O"+Fore.WHITE+"O"+Fore.BLUE+"K"+Fore.GREEN+"U"+Fore.RED+"P"+Fore.RED+"]"+"""
  └─$ """+Fore.WHITE)
        req = requests.get("https://api.hackertarget.com/dnslookup/?q="+target).text
        out =input(" \n   Do You Want To Save The Output? yes/no  ")
        if out == "Yes" or out =="yes":
            map = "C:\\Users\\"+user+"\\Desktop\\"
            file=open(map+"DNSLookup - "+target+".txt","w")
            file.write(str(req))
            time.sleep(0.5)
            print(Fore.CYAN+"\n   /"+Fore.RED+"+"+Fore.GREEN+"\   "+Fore.WHITE+"'Check Desktop'\n")
        elif out == "no" or out == "No":
            print("\n"+Fore.WHITE+req)

        try:
            input(Fore.BLUE+"   /"+Fore.GREEN+"M"+Fore.LIGHTCYAN_EX+"\   "+Fore.WHITE+"Back To Menu (Press Enter...) ")
        except:
             print("")
             sys.exit()

    except:
        print("")
        sys.exit()



