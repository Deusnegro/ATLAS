import requests
import sys
from colorama import Fore,init
import time 
import getpass
init()
user = getpass.getuser()
def __start__():
    
    try:
        print(Fore.GREEN+"   /"+Fore.RED+"+"+Fore.GREEN+"\   "+Fore.WHITE+"Please Enter Domain/IP\n ")
        
        target = input(Fore.RED+" ┌──("+Fore.WHITE+"kali"+Fore.BLUE+"㉿"+Fore.WHITE+"kali"+Fore.RED+")"+Fore.WHITE+'-'+Fore.RED+"["+Fore.WHITE+"~/"+Fore.LIGHTMAGENTA_EX+"A"+Fore.LIGHTCYAN_EX+"T"+Fore.LIGHTRED_EX+"L"+Fore.YELLOW+"A"+Fore.BLUE+"S"+Fore.RED+"/"+Fore.WHITE+"M"+Fore.BLUE+"E"+Fore.GREEN+"N"+Fore.RED+"O"+Fore.YELLOW+"/"+Fore.LIGHTCYAN_EX+"I"+Fore.RED+"G"+Fore.LIGHTMAGENTA_EX+"/"+Fore.LIGHTCYAN_EX+"H"+Fore.LIGHTRED_EX+"T"+Fore.LIGHTMAGENTA_EX+"T"+Fore.LIGHTCYAN_EX+"P"+Fore.LIGHTRED_EX+"H"+Fore.YELLOW+"E"+Fore.BLUE+"A"+Fore.RED+"D"+Fore.WHITE+"E"+Fore.BLUE+"R"+Fore.RED+"]"+"""
 └─$ """+Fore.WHITE)
        req = requests.get("https://api.hackertarget.com/httpheaders/?q="+target).text
        out =input(" \n   Do You Want To Save The Output? yes/no  ")
        if out == "Yes" or out =="yes":
            map = "C:\\Users\\"+user+"\\Desktop\\"
            file=open(map+"HTTPHeder - "+target+".txt","w")
            file.write(str(req))
            time.sleep(0.5)
            print(Fore.CYAN+"\n   /"+Fore.RED+"+"+Fore.GREEN+"\   "+Fore.WHITE+"'Check Desktop'\n")
        elif out == "no" or out == "No":
            print("\n"+Fore.WHITE+req)
        try:
            input(Fore.MAGENTA+"   /"+Fore.YELLOW+"M"+Fore.GREEN+"\   "+Fore.WHITE+"Back To Menu (Press Enter...) ")
        except:
             print("")
             sys.exit()

    except:
        print("")
        sys.exit()


