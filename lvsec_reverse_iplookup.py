import os
import sys
import threading
import socket
import termcolor as tm
import signal
import pyfiglet
import requests

def sig_handler(recieved_sig, frame):
	print("\nCtr-C detected, Exiting..............!")
	sys.exit(0)

signal.signal(signal.SIGINT, sig_handler)
def print_banner():
	figfont = 'xtty' #you can list fonts by typing pyfiglet --list fonts
	figinit = pyfiglet.Figlet(font=figfont)
	lv_banner = "LVSEC"
	print(tm.colored(figinit.renderText(lv_banner),'yellow'))

print_banner()

def lookup(ip):
	res = requests.get(url=f"https://api.hackertarget.com/reverseiplookup/?q={ip}",verify=True,allow_redirects=True)
	print(res.text)

if __name__ == "__main__":
	lookup(str(sys.argv[1]))
