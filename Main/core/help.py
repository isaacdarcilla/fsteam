#!/usr/bin/python

import os
from colored import *

def help():
	print "\n \033[1;31mGeneral Commands\tDescription\033[1;m\n\tversion\t\tprints script version\n\thelp\t\tprints this help\n\tcredits\t\tprints script developers\n\tclear\t\tclears terminal sessions\n\tclean\t\tclears log and history\n\tdownload\tdirectly download update\n\tupgrade\t\tget to the latest version\n\tabout\t\tlet me tell you something\n\texit\t\tcloses command sessions\n\n \033[1;31mModule Commands\tDescriptions\033[1;m\n\tshow modules\tprints all available modules\n\tshow updates\tprints upcoming modules\n\tshow devices\tprint acquired address\n\tshow changelog\tprint the change log\n\tuse  [module]\tload an existing module\t\n\n \033[1;31mNetwork Commands\tDescriptions\033[1;m\n\tmonitor on\tenable monitor mode\n\tmonitor off\tdisable monitor mode\n\tifconfig\tview available network adapter\n\tiwconfig\tview which adapter is in monitor mode\n"
