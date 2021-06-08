import os
from subprocess import Popen,check_output
import sys
import getpass
from colorama import Fore
import time
import platform
import PyInstaller.__main__
users=getpass.getuser()
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
def buldexe():
    banner()
    print(Fore.RED+"\n   /"+Fore.YELLOW+"+"+Fore.BLUE+"\   "+Fore.WHITE+"Place Enter The File Name ==> Simple: file.py")
    print(Fore.CYAN+"   /"+Fore.GREEN+"+"+Fore.MAGENTA+"\   "+Fore.WHITE+"Directory : /Desktop \n")
    try:
        file_name = input(Fore.RED+"  ┌──("+Fore.WHITE+"kali"+Fore.BLUE+"㉿"+Fore.WHITE+"kali"+Fore.RED+")"+Fore.WHITE+'-'+Fore.RED+"["+Fore.WHITE+"~/"+Fore.LIGHTMAGENTA_EX+"A"+Fore.LIGHTCYAN_EX+"T"+Fore.LIGHTRED_EX+"L"+Fore.YELLOW+"A"+Fore.BLUE+"S"+Fore.RED+"/"+Fore.WHITE+"M"+Fore.BLUE+"E"+Fore.GREEN+"N"+Fore.RED+"O"+Fore.YELLOW+"/"+Fore.LIGHTCYAN_EX+"V"+Fore.RED+"S"+Fore.LIGHTMAGENTA_EX+"/"+Fore.LIGHTCYAN_EX+""+Fore.LIGHTRED_EX+"E"+Fore.YELLOW+"N"+Fore.BLUE+"T"+Fore.RED+"E"+Fore.WHITE+"R"+Fore.CYAN+"-"+Fore.BLUE+"N"+Fore.GREEN+"A"+Fore.RED+"M"+Fore.YELLOW+"E"+Fore.RED+"]"+"""
  └─$ """+Fore.WHITE)
    except KeyboardInterrupt:
        print("")
        sys.exit()
    if file_name == "":
        print(Fore.WHITE+"\n   /"+Fore.RED+"!"+Fore.WHITE+"\   "+Fore.WHITE+"Please Enter Icon Data !!")
        sys.exit()
    else:
        pass
    banner()
    try: 
        print(Fore.BLUE+"\n   /"+Fore.WHITE+"+"+Fore.GREEN+"\   "+Fore.WHITE+"Please Enter The Number Icon  ==> Simple: 25 \n")
        
        print(Fore.BLUE+"""\n   /"""+Fore.WHITE+"""+"""+Fore.GREEN+"""\   """+Fore.RED+"""Select Icon :\n 
        /01\ Excel           /11\ WordPress    /21\ Game Matrix
        /02\ PDF             /12\ VMware       /22\ Game GTA    
        /03\ RAR             /13\ Safari       /23\ Game GTA 3
        /04\ PowerPoint      /14\ PowerDVD     /24\ Game Drivers 2
        /05\ Word            /15\ OneNote      /25\ Game CallOfDuty
        /06\ Chrome          /16\ Lync         /26\ Game CartingGran
        /07\ 7zip            /17\ joomla       /27\ Game GTA 4
        /08\ AdobeAfter      /18\ GoogleDrive  /28\ Game Aztec Gold
        /09\ AdobePhotoshop  /19\ Calculator   /29\ Apache
        /10\ AntiVirus       /20\ Bluetooth    /30\ Adobe Flash\n
        """)
        icon_number = input(Fore.RED+"  ┌──("+Fore.WHITE+"kali"+Fore.BLUE+"㉿"+Fore.WHITE+"kali"+Fore.RED+")"+Fore.WHITE+'-'+Fore.RED+"["+Fore.WHITE+"~/"+Fore.LIGHTMAGENTA_EX+"A"+Fore.LIGHTCYAN_EX+"T"+Fore.LIGHTRED_EX+"L"+Fore.YELLOW+"A"+Fore.BLUE+"S"+Fore.RED+"/"+Fore.WHITE+"M"+Fore.BLUE+"E"+Fore.GREEN+"N"+Fore.RED+"O"+Fore.YELLOW+"/"+Fore.LIGHTCYAN_EX+"V"+Fore.RED+"S"+Fore.LIGHTMAGENTA_EX+"/"+Fore.LIGHTCYAN_EX+""+Fore.LIGHTRED_EX+"E"+Fore.YELLOW+"N"+Fore.BLUE+"T"+Fore.RED+"E"+Fore.WHITE+"R"+Fore.CYAN+"-"+Fore.BLUE+"I"+Fore.GREEN+"C"+Fore.RED+"O"+Fore.YELLOW+"N"+Fore.RED+"]"+"""
  └─$ """+Fore.WHITE)
        if icon_number == "":
            print(Fore.WHITE+"\n   /"+Fore.RED+"!"+Fore.WHITE+"\   "+Fore.WHITE+"Please Enter Icon Data !!")
            sys.exit()
        else:
            pass
        icon_name = ()
        if icon_number == "1":
            icon_name = "excel.ico"
        elif icon_number == "2":
            icon_name = "pdf.ico"
        elif icon_number == "3":
            icon_name = "rar.ico"
        elif icon_number == "4":
            icon_name = "PowerPoint.ico"
        elif icon_number == "5":
            icon_name = "word.ico"
        elif icon_number == "6":
            icon_name = "chrome.ico"
        elif icon_number == "7":
            icon_name = "7zip_alt.ico"
        elif icon_number == "8":
            icon_name = "Adobe-After-Effects.ico"
        elif icon_number == "9":
            icon_name = "Adobe-Photoshop.ico"
        elif icon_number == "10":
            icon_name = "Anti-Virus.ico"   
        elif icon_number == "11":
            icon_name = "wordpress.ico" 
        elif icon_number == "12":
            icon_name = "vmware_player.ico"
        elif icon_number == "13":
            icon_name = "safari.ico"
        elif icon_number == "14":
            icon_name = "powerdvd.ico"
        elif icon_number == "15":
            icon_name = "OneNote.ico"
        elif icon_number == "16":
            icon_name = "Lync.ico"
        elif icon_number == "17":
            icon_name = "joomla_blue.ico"
        elif icon_number == "18":
            icon_name = "google_drive.ico"
        elif icon_number == "19":
            icon_name = "calculator.ico"
        elif icon_number == "20":
            icon_name = "Bluetooth.ico"
        elif icon_number == "21":
            icon_name = "Matrix.ico"
        elif icon_number == "22":
            icon_name = "gta_vice_city_small_3.ico"
        elif icon_number == "23":
            icon_name = "GTA_3.ico"
        elif icon_number == "24":
            icon_name = "Drivers_2.ico"
        elif icon_number == "25":
            icon_name = "CallOfDuty.ico"
        elif icon_number == "26":
            icon_name = "Carting_Gran_Pri.ico"
        elif icon_number == "27":
            icon_name = "app.ico"
        elif icon_number == "28":
            icon_name = "Aztec Gold"
        elif icon_number == "29":
            icon_name = "apache.ico"
        elif icon_number == "30":
            icon_name = "adobe_flash.ico"
    except KeyboardInterrupt:
        print("")
        sys.exit()
    banner()

    PyInstaller.__main__.run([
    '-F',
    'C:\\Users\\'+users+'\\Desktop\\'+file_name,
    '-i',
    'icon\\'+icon_name,
    ])

    banner()
    time.sleep(5)
    print(Fore.GREEN+"\n   /"+Fore.YELLOW+"+"+Fore.BLUE+"\   "+Fore.WHITE+"exe File in ==> /ATLAS/dist/"+file_name+ "Directory")
    time.sleep(2)
    try:
       input(Fore.BLUE+"\n   /"+Fore.YELLOW+"M"+Fore.MAGENTA+"\   "+Fore.WHITE+"Back To Menu (Press Enter...)")
    except:
        print("")
        sys.exit()


