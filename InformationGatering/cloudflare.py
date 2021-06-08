import socket
import sys
import time
from colorama import Fore,init



def __start__():

    init()

    print(Fore.RED+"   /"+Fore.YELLOW+"01"+Fore.BLUE+"\   "+Fore.WHITE+"Please Enter The Target Website Address\n")
    subdom = ("""ftp
cpanel
webmail
localhost
local 
mysql 
forum
driect-connect
blog 
vb
forums
home
direct
forums
mail
access
admin
administrator
email
downloads
ssh
owa
bbs
webmin
paralel
parallels
www0
www
www1
www2
www3
www4
www5
shop
api
blogs
test
mx1
cdn 
mysql
mail1
secure
server
ns1
ns2
smtp
vpn
m
mail2 
postal
support
web
dev
""").split()
    site = input(Fore.RED+"  ┌──("+Fore.WHITE+"kali"+Fore.BLUE+"㉿"+Fore.WHITE+"kali"+Fore.RED+")"+Fore.WHITE+'-'+Fore.RED+"["+Fore.WHITE+"~/"+Fore.LIGHTMAGENTA_EX+"A"+Fore.LIGHTCYAN_EX+"T"+Fore.LIGHTRED_EX+"L"+Fore.YELLOW+"A"+Fore.BLUE+"S"+Fore.RED+"/"+Fore.WHITE+"M"+Fore.BLUE+"E"+Fore.GREEN+"N"+Fore.RED+"O"+Fore.YELLOW+"/"+Fore.LIGHTCYAN_EX+"I"+Fore.RED+"G"+Fore.LIGHTMAGENTA_EX+"/"+Fore.LIGHTCYAN_EX+"B"+Fore.LIGHTRED_EX+"A"+Fore.YELLOW+"Y"+Fore.BLUE+"P"+Fore.RED+"A"+Fore.WHITE+"S"+Fore.BLUE+"S"+Fore.GREEN+" C"+Fore.RED+"O"+Fore.YELLOW+"U"+Fore.LIGHTCYAN_EX+"D"+Fore.RED+"F"+Fore.LIGHTMAGENTA_EX+"L"+Fore.LIGHTCYAN_EX+"A"+Fore.LIGHTRED_EX+"R"+Fore.YELLOW+"E"+Fore.BLUE+Fore.RED+"]"+"""
  └─$ """+Fore.WHITE)
    
    

    if site == "":
        try:
            print(Fore.WHITE+"   /"+Fore.GREEN+"-"+Fore.BLUE+"\   "+Fore.WHITE+"Please Enter Address :) \n")
            time.sleep(5)
            sys.exit()
        except:
            return
    print("")
    


    for sub in subdom:
        try:
            hosts = str(sub) + "." + str(site)
            bypass = socket.gethostbyname(str(hosts))
            #print('Cloudflare Bypassed ! Real IP Address => '+bypass)
            print (Fore.GREEN+"   /+\   "+Fore.YELLOW+"CloudFlare Bypass"+Fore.WHITE+ str(bypass) +Fore.YELLOW+ ' | '+Fore.WHITE+ str(hosts))
        except Exception:
            pass


    try:
        
        input(Fore.BLUE+"\n   /"+Fore.YELLOW+"M"+Fore.MAGENTA+"\   "+Fore.WHITE+"Back To Menu (Press Enter...)")
    except:
        print("")
        sys.exit()



