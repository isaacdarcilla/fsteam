#!/usr/bin/env python


import os
import urllib
from time import *
from colored import *

def upgrade():
	print("[+] Checking repos for a new version. Please wait.")
	sleep(2)
	try:
		cu = urllib.urlopen("https://github.com/isaacdarcilla/fsteam/pkg")  #im going to replace this link
		res = cu.read()
		if 'Fsecurity Framework 0.1.8 CodeFish' in res:
			print("[+] New version of \fsecurity framework\' is available.")
			sleep(2)
			print("[+] Download: https://github.com/isaacdarcilla/fsteam/pkg/framework-0.1.9-codefish.tar.gz")
			print("[+] Starting browser. Please wait.")
			sleep(2)
			os.system('iceweasel https://github.com/isaacdarcilla/fsteam/pkg/framework-0.1.9-codefish.tar.gz')
			os.system('chrome https://github.com/isaacdarcilla/fsteam/pkg/framework-0.1.9-codefish.tar.gz')
		else:
			print("[-] No new version of \'fsecurity framework\' is available.\nThis is the latest version of \'fsecurity framework.\'")
		   	sleep(4)
	except(IOError):
		print("[-] Error Found: No internet connection. ")
	except KeyboardInterrupt:
		print""
