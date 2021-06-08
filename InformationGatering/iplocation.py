import requests
import os
import sys
import ipapi
from colorama import Fore,init
import time
import socket

def __start__():
    init()
    print(Fore.WHITE+"   /"+Fore.RED+"+"+Fore.BLUE+"\   "+Fore.WHITE+"Enter IP Address or Domain \n")
    
    site = input(Fore.RED+" ┌──("+Fore.WHITE+"kali"+Fore.BLUE+"㉿"+Fore.WHITE+"kali"+Fore.RED+")"+Fore.WHITE+'-'+Fore.RED+"["+Fore.WHITE+"~/"+Fore.LIGHTMAGENTA_EX+"A"+Fore.LIGHTCYAN_EX+"T"+Fore.LIGHTRED_EX+"L"+Fore.YELLOW+"A"+Fore.BLUE+"S"+Fore.RED+"/"+Fore.WHITE+"M"+Fore.BLUE+"E"+Fore.GREEN+"N"+Fore.RED+"O"+Fore.YELLOW+"/"+Fore.LIGHTCYAN_EX+"I"+Fore.RED+"G"+Fore.LIGHTMAGENTA_EX+"/"+Fore.LIGHTCYAN_EX+"I"+Fore.LIGHTRED_EX+"P"+Fore.LIGHTMAGENTA_EX+"L"+Fore.LIGHTCYAN_EX+"C"+Fore.LIGHTRED_EX+"A"+Fore.YELLOW+"T"+Fore.BLUE+"I"+Fore.RED+"O"+Fore.WHITE+"N"+Fore.RED+"]"+"""
 └─$ """+Fore.WHITE)

    taeget = socket.gethostbyname(site)
    source = ipapi.location(ip=taeget)
    try:
        print (Fore.BLUE+"\n   /"+Fore.CYAN+"M"+Fore.GREEN+"\   "+Fore.WHITE+" Please Wait While loading\n")
        time.sleep(5)
        print (Fore.GREEN+"   /+\  "+Fore.WHITE+" ip = "+ source["ip"])
        print (Fore.GREEN+"   /+\  "+Fore.WHITE+" version = "+ source["version"])
        print (Fore.GREEN+"   /+\  "+Fore.WHITE+" id country = "+source["country"])
        print (Fore.GREEN+"   /+\  "+Fore.WHITE+" country = "+ source["country_name"])
        print (Fore.GREEN+"   /+\  "+Fore.WHITE+" Calling Code = "+source["country_calling_code"])
        print (Fore.GREEN+"   /+\  "+Fore.WHITE+" country_code = "+ source["country_code"])
        print (Fore.GREEN+"   /+\  "+Fore.WHITE+" country_code_iso3 = "+ source["country_code_iso3"])
        print (Fore.GREEN+"   /+\  "+Fore.WHITE+" Languages = "+source["languages"])
        print (Fore.GREEN+"   /+\  "+Fore.WHITE+" city = " + source["city"])
        print (Fore.GREEN+"   /+\  "+Fore.WHITE+" region_code = "+ source["region_code"])
        print (Fore.GREEN+"   /+\  "+Fore.WHITE+" region = "+ source["region"])
        print (Fore.GREEN+"   /+\  "+Fore.WHITE+" org = "+ source["org"])
        print (Fore.GREEN+"   /+\  "+Fore.WHITE+" asn = "+ source["asn"])
        print (Fore.GREEN+"   /+\  "+Fore.WHITE+" currency_name = "+ source["currency_name"])
        print (Fore.GREEN+"   /+\  "+Fore.WHITE+" currency = "+ source["currency"])
        # print (Fore.GREEN+" [+]"+Fore.WHITE+" postal = "+ source["postal"])
        print (Fore.GREEN+"   /+\  "+Fore.WHITE+" utc_offset = "+ source["utc_offset"]+"\n")
        try:
            input(Fore.BLUE+"\n   /"+Fore.LIGHTYELLOW_EX+"M"+Fore.RED+"\   "+Fore.WHITE+"Back To Menu (Press Enter...) ")
        except:
            print("")
            sys.exit()  
    except:
        print(Fore.WHITE+"Sorry Please Enter IP Address")
        sys.exit()



