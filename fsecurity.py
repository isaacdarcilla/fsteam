
#!/usr/bin/python

# coding: utf-8
# Copyright (c) 2016 Free Security Team
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#


import os
import sys
import shutil
import readline
sys.path.append('Main')
#python2.7/bin/dist-upgrade
from socket import *
from time import *
from mechanize import *
from colored import *
from threading import *
#framework/Main/core
from os.path import exists
from Main.core import modules
from Main.core import header
from Main.core import upgrade
from Main.core import help
from Main.core import version
from Main.core import _modules
from Main.core import credits
from Main.core import about
from Main.core import download
from Main.core import address

print fore.YELLOW+"Loading.."+style.RESET
try:
	print '\033[1;31m\nWaiting for a script kiddie to piss off. Please wait.\n\033[1;m '
	troll = str(raw_input("")) #troll level: GOD
except KeyboardInterrupt:
	print  (fore.BLUE+'[-] Aww, giving up already?'+style.RESET)
	exit()
os.system("clear")
date=os.system('date')

def main():
	try:
		user_input = ('%s[CMD-LINE] %s' % (fg(1), attr(0)))
		user_input += ": "
		terminal = raw_input(user_input)
		#CORE COMMANDS
		if terminal[0:3] =='use':
			if terminal[4:20] =='net/cookiehijack':
				os.system('sudo python Main/cookieHijack.pyc')
				main()
			elif terminal[4:27] =='wifi/decloaker':
				os.system('sudo python Main/hiddenNetworkSniffer.pyc')
				main()
			elif terminal[4:20] =='net/ftpscanner':
				os.system('sudo python Main/ftpScanner.pyc')
				main()
			elif terminal[4:20] =='net/portscanner':
				os.system('sudo python Main/nmapIntegrator.pyc')
				main()
			elif terminal[4:27] =='net/packetsniffer':
				os.system('sudo python Main/packetSnifferScapy.pyc')
				main()
			elif terminal[4:28] =='server/ftpserver':
				os.system('sudo python Main/ftpServerExec.pyc')
				main()
			elif terminal[4:29] =='net/probesniffer':
				os.system('sudo python Main/probeSniffer.pyc')
				main()
			elif terminal[4:30] =='file/filecracker':
				os.system('sudo python Main/zipFileCracker.pyc')
				main()
			elif terminal[4:31] =='web/webbrowser':
				os.system('sudo python Main/anonWebBrowser.pyc')
				main()
			elif terminal[4:32] =='wifi/ccsniffer':
				print fore.BLUE+"[-] Module deprecated. Read why https://github.com/tuxdeflux/modules/deprecated/"+style.RESET
				main()
			elif terminal[4:33] =='web/domain':
				os.system('sudo python Main/domainDetector.pyc')
				main()
			elif terminal[4:33] =='web/fastflux':
				os.system('sudo python Main/fastFluxDetector.pyc')
				main()
			elif terminal[4:34] =='web/iplocate':
				os.system('sudo python Main/ipGeolocate.pyc')
				main()
			elif terminal[4:35] =='net/networksniffer':
				os.system('sudo python Main/networkSniffer.pyc')
				main()
			elif terminal[4:36] =='bluetooth/macbtid':
				os.system('sudo python Main/bluetoothIphone.pyc')
				main()
			elif terminal[4:37] =='bluetooth/btrfcomm':
				os.system('sudo python Main/bluetoothRfcomm.pyc')
				main()
			elif terminal[4:38] =='bluetooth/btsdp':
				os.system('sudo python Main/bluetoothServiceDiscovery.pyc')
				main()
			elif terminal[4:39] =='bluetooth/btsniffer':
				os.system('sudo python Main/bluetoothSniffer.py')
				main()
			else:
				print fore.BLUE+"[-] No such module. Type \'show modules\' to view modules."+style.RESET
				main()

			main()
		elif terminal[0:12] =='upgrade':
			upgrade.upgrade()
			main()
		elif terminal[0:10] =='version':
			version.version()
			main()
		elif terminal[0:12] =='help':
			help.help()
			main()
		elif terminal[0:12] =='show modules':
			modules.modules()
			main()
		elif terminal[0:13] =='show updates':
			_modules._modules()
			main()
		elif terminal[0:7] =='clear':
			os.system('clear')
			main()
		elif terminal[0:5] =='clean':
			os.system('sudo bash Main/_logger.sh')
			os.system('sudo bash Main/_cleaner.sh')
			main()
		elif terminal[0:9] =='credits':
			credits.credits()
			main()
		elif terminal[0:14] =='about':
			about.about()
			main()
		elif terminal[0:54] =='monitor on':
			os.system('sudo bash Main/core/bash/monitorenabled.sh')
			main()
		elif terminal[0:55] =='monitor off':
			os.system('sudo bash Main/core/bash/monitordisabled.sh')
			main()
		elif terminal[0:56] =='ifconfig':
			print " "
			os.system('sudo ifconfig')
			main()
		elif terminal[0:57] =='iwconfig':
			print " "
			os.system('sudo iwconfig')
			main()
		elif terminal[0:58] == 'banner':
			os.system('sudo bash Main/headers/header.sh')
			main()
		elif terminal[0:61] == 'download':
			download.download()
			main()
		elif terminal[0:62] == 'show devices':
			address.address()
			main()
		elif terminal[0:63] == 'show changelog':
			os.system('sudo cat README/CHANGELOG.md')
			main()
		elif terminal[0:6] =='exit':
			exit()
			try:
				# kill anything python running on 80
				kill_proc("80","python")
                # kill anything on 443 which is generally a rogue listener
				kill_proc("443", "ruby")
				os.system('clear')
			except: pass
		else :
			print fore.BLUE+"[-] No such command:"+style.RESET,terminal
			main()

	except KeyboardInterrupt:
		print  ('\n\n'+fore.BLUE+'[+] Terminating framework session. Please wait.\n'+style.RESET)
		sleep(3)
		os.system('clear');
		os.system('date');
		exit()
def start():
	os.system('sudo bash Main/headers/header.sh')
	main()
if __name__=='__main__':
    start()
