import os
import requests
import json
from colorama import Fore
import sys

def __start__():
 try:        
        
        print (Fore.CYAN+"   /"+Fore.YELLOW+"+"+Fore.RED+"\   "+Fore.WHITE+"Enter The Domain / IP\n")
        website = input(Fore.RED+"  ┌──("+Fore.WHITE+"kali"+Fore.BLUE+"㉿"+Fore.WHITE+"kali"+Fore.RED+")"+Fore.WHITE+'-'+Fore.RED+"["+Fore.WHITE+"~/"+Fore.LIGHTMAGENTA_EX+"A"+Fore.LIGHTCYAN_EX+"T"+Fore.LIGHTRED_EX+"L"+Fore.YELLOW+"A"+Fore.BLUE+"S"+Fore.RED+"/"+Fore.WHITE+"M"+Fore.BLUE+"E"+Fore.GREEN+"N"+Fore.RED+"O"+Fore.YELLOW+"/"+Fore.LIGHTCYAN_EX+"I"+Fore.RED+"G"+Fore.LIGHTMAGENTA_EX+"/"+Fore.LIGHTCYAN_EX+"R"+Fore.LIGHTRED_EX+"E"+Fore.LIGHTMAGENTA_EX+"V"+Fore.LIGHTCYAN_EX+"E"+Fore.LIGHTRED_EX+"R"+Fore.YELLOW+"S"+Fore.BLUE+"E"+Fore.RED+"I"+Fore.WHITE+"P"+Fore.RED+"]"+"""
  └─$ """+Fore.WHITE)
        mysite = {"remoteAddress":website}
        link = requests.post("https://domains.yougetsignal.com/domains.php" , mysite)
        source = json.loads(link.content)
        print("")
        for data in source["domainArray"]:
                print(Fore.GREEN+"   \+/   "+Fore.WHITE+data[0])
        try:
            input(Fore.GREEN+"\n   /"+Fore.MAGENTA+"M"+Fore.RED+"\   "+Fore.WHITE+"Back To Menu (Press Enter...) ")
        except:
             print("")
             sys.exit()
 except:
         print("")
         sys.exit()