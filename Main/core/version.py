#!/usr/bin/python
import os
from colored import *
import upgrade

def version():
	print fore.BLUE+"   FSECURITY FRAMEWORK version \'0.1.9\'\n   (c) Free Security Team [http://web.fsec.ty]\n   Visit our website for more info.\n"+style.RESET
	check=str(raw_input(fore.YELLOW+"   Check for update [Y|N] "+style.RESET))
	if (check == 'Y') | (check == 'y'):
		print " "
		upgrade.upgrade()
	else:
		pass 
