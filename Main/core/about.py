#!/usr/bin/python

import os
from colored import *

def about():
	print fore.BLUE+'   FSECURITY FRAMEWORK'
	print fore.GREEN+'   Free Security Team\n'+style.RESET 
	print '    Version: 0.1.9' 
	print ' Build Date: November 5, 2016'
	print '  Code Name: \'Code Fish\''+style.RESET

	license = str(raw_input(fore.YELLOW+'   View License [Y|N] '+style.RESET))
	if (license == 'Y') | (license == 'y'):
		print " "
		os.system('cat Main/license/license.txt')
		cont = str(raw_input(''))
	else:
		pass
