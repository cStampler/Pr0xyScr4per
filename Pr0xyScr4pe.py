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
║Pr0xyScr4pe                                  ║
║Dsicord: stampler#9931 for contact           ║
╚═════════════════════════════════════════════╝
'''



print(Fore.RED+info)
print(Fore.CYAN+icon)


print()
ready = input(f'{Fore.YELLOW} This will generate 1k of each proxy type. (Hit "ENTER" To Continue) ')

url1 = 'https://api.openproxylist.xyz/http.txt'
url2 = 'https://www.proxy-list.download/api/v1/get?type=http'
r1 = requests.get(url1)
r2 = requests.get(url2)
results1 = r1.text
results2 = r2.text
with open ("http.txt", "w") as file:
 file.write(results1)
 file.write(results2)
 
url = 'https://api.openproxylist.xyz/socks4.txt'
r = requests.get(url)
results = r.text
with open ("socks4.txt", "w") as file:
 file.write(results)
 
url = 'https://api.openproxylist.xyz/socks5.txt'
r = requests.get(url)
results = r.text
with open ("socks5.txt", "w") as file:
 file.write(results)