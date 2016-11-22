#!/usr/bin/python

import os
from colored import *
from time import *
def download():
	try:

		link = str(raw_input("%s[CMD-LINE]:[LINK]: %s"%(fg(1), attr(0))))
		print (fore.LIGHT_BLUE+"LINK:["+style.RESET+link+fore.LIGHT_BLUE+']\n'+style.RESET)
		print fore.WHITE+"[+] Downloading. Please wait.\n"+style.RESET
		sleep (2)
		os.system("sudo wget --quiet "+link)
	except(IOError):
		print("[-] Error Found: No internet connection. ")		
