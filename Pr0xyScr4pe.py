import os
from time import sleep
import requests
import random
import string
from colorama import Fore
import webbrowser



os.system('cls')

icon = '''
__________         _______                  _________               _____                
\______   \_______ \   _  \ ___  ______.__./   _____/ ___________  /  |  |______   ____  
 |     ___/\_  __ \/  /_\  \\  \/  <   |  |\_____  \_/ ___\_  __ \/   |  |\____ \_/ __ \ 
 |    |     |  | \/\  \_/   \>    < \___  |/        \  \___|  | \/    ^   /  |_> >  ___/ 
 |____|     |__|    \_____  /__/\_ \/ ____/_______  /\___  >__|  \____   ||   __/ \___  >
                          \/      \/\/            \/     \/           |__||__|        \/ 
'''

info = '''
╔═════════════════════════════════════════════╗
║Pr0xyScr4pe    Refreshed Daily               ║
║Dsicord: stampler#9931 for contact           ║
╚═════════════════════════════════════════════╝
'''
print(Fore.RED+info)
print(Fore.CYAN+icon)


print()
ready = input(f'{Fore.YELLOW} This will generate roughly 1k or more of each proxy type. (Hit "ENTER" To Continue) ')

url1 = 'https://api.openproxylist.xyz/http.txt'
url2 = 'https://www.proxy-list.download/api/v1/get?type=http'
r1 = requests.get(url1)
r2 = requests.get(url2)
results1 = r1.text
results2 = r2.text
with open ("http.txt", "w") as file:
 file.write(results1 + results2)



url1 = 'https://www.proxy-list.download/api/v1/get?type=https'
url2 = 'https://www.proxy-list.download/api/v1/get?type=https'
r1 = requests.get(url1)
r2 = requests.get(url2)
results1 = r1.text
results2 = r2.text
with open ("https.txt", "w") as file:
 file.write(results1 + results2)



url1 = 'https://www.proxy-list.download/api/v1/get?type=https&anon=elite'
url2 = 'https://www.proxy-list.download/api/v1/get?type=https&anon=elite'
r1 = requests.get(url1)
r2 = requests.get(url2)
results1 = r1.text
results2 = r2.text
with open ("elitehttps.txt", "w") as file:
 file.write(results1 + results2)


url1 = 'https://www.proxy-list.download/api/v1/get?type=https&anon=elite&country=US'
url2 = 'https://www.proxy-list.download/api/v1/get?type=https&anon=elite&country=US'
r1 = requests.get(url1)
r2 = requests.get(url2)
results1 = r1.text
results2 = r2.text
with open ("eliteusahttps.txt", "w") as file:
 file.write(results1 + results2)



 
url1 = 'https://api.openproxylist.xyz/socks4.txt'
url2 = 'https://www.proxy-list.download/api/v1/get?type=socks4'
r1 = requests.get(url1)
r2 = requests.get(url2)
results1 = r1.text
results2 = r2.text
with open ("socks4.txt", "w") as file:
 file.write(results1 + results2)
 
url1 = 'https://api.openproxylist.xyz/socks5.txt'
url2 = 'https://www.proxy-list.download/api/v1/get?type=socks5'
r1 = requests.get(url1)
r2 = requests.get(url2)
results1 = r1.text
results2 = r2.text
with open ("socks5.txt", "w") as file:
 file.write(results1 + results2)