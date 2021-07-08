from sys import platform
import requests 
import time as t
import os
 
Times = 1
Choice = input(' 1 For Https/s, 2 For Socks4, 3 For Socks5 : ')
print('\n')
if Choice == '1':
           Url = 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all'

elif Choice == '2':

		Url = 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all'

elif Choice == '3':

    Url = 'https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks5&timeout=10000&country=all'

else:
    print('\x1b[0;31;49m' + ' Wrong Choice ' + '\x1b[0m')
    exit(0)
while 1:
    print ('\x1b[0;34;49m' + ' Programmed By : https://instagram.com/6o9s\n\n ' + '\x1b[0m') 
    r = requests.get(Url)
    append = open('Proxies.txt', 'a')
    append.write(r.text)
    print(f' Proxies Downloaded : {Times} Times\n\n')
    Times = Times + 1
    t.sleep(60)
    if platform == 'linux' or 'darwin':
        os.system('clear')
    else:
        os.system('cls')