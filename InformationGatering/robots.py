import requests
import sys
import time
from colorama import Fore
search = ['robots.txt',
'search/',
'admin/',
'login/',
'sitemap.xml',
'sitemap2.xml',
'config.php',
'wp-login.php',
'log.txt',
'update.php',
'INSTALL.pgsql.txt',
'user/login/',
'INSTALL.txt',
'profiles/',
'scripts/',
'LICENSE.txt',
'CHANGELOG.txt',
'themes/',
'inculdes/',
'misc/',
'user/logout/',
'user/register/',
'cron.php',
'filter/tips/',
'comment/reply/',
'xmlrpc.php',
'modules/',
'install.php',
'MAINTAINERS.txt',
'user/password/',
'node/add/',
'INSTALL.sqlite.txt',
'UPGRADE.txt',
'INSTALL.mysql.txt']

def __start__():
    try:
        print(Fore.WHITE+"   /"+Fore.RED+"+"+Fore.GREEN+"\   "+Fore.WHITE+"Plase Enter WebSite Address \n")
        url = input(Fore.RED+"  ┌──("+Fore.WHITE+"kali"+Fore.BLUE+"㉿"+Fore.WHITE+"kali"+Fore.RED+")"+Fore.WHITE+'-'+Fore.RED+"["+Fore.WHITE+"~/"+Fore.LIGHTMAGENTA_EX+"A"+Fore.LIGHTCYAN_EX+"T"+Fore.LIGHTRED_EX+"L"+Fore.YELLOW+"A"+Fore.BLUE+"S"+Fore.RED+"/"+Fore.WHITE+"M"+Fore.BLUE+"E"+Fore.GREEN+"N"+Fore.RED+"O"+Fore.YELLOW+"/"+Fore.LIGHTCYAN_EX+"I"+Fore.RED+"G"+Fore.LIGHTMAGENTA_EX+"/"+Fore.LIGHTCYAN_EX+"R"+Fore.LIGHTRED_EX+"O"+Fore.LIGHTMAGENTA_EX+"B"+Fore.LIGHTCYAN_EX+"O"+Fore.LIGHTRED_EX+"T"+Fore.YELLOW+"S"+Fore.RED+"]"+"""
  └─$ """+Fore.WHITE)
        print("")
        if 'http' in url:
            pass
        elif 'http' != url:
            url = ('http://'+url)
            
        for i in search:
            time.sleep(0.1)

            ur = (url+"/"+i)
            "http://pythons.ir/robots.txt"
            reqs = requests.get(ur)
            if reqs.status_code == 200 or reqs.status_code == 405:
                print(Fore.GREEN+"   \+/   "+Fore.WHITE+ ur)
            else:
                print(Fore.RED+"   \-/   "+Fore.WHITE+ur)
        try:
            input(Fore.BLUE+"\n   /"+Fore.WHITE+"M"+Fore.GREEN+"\   "+Fore.WHITE+"Back To Menu (Press Enter...) ")
        except:
            print("")
            sys.exit()  
    except:
        print("")
        sys.exit()