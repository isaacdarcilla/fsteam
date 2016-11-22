#!/usr/bin/python
#bluetooth mac address

import os
from os.path import exists
from colored import *
def address():
	if exists('Main/core/logs/_btlogs.txt'):
		fileName = file('Main/core/logs/_btlogs.txt', 'r')		
		print fileName.read()


	if exists('Main/core/logs/_iplogs.txt'):
		fileName2 = file('Main/core/logs/_iplogs.txt', 'r')		
		print fileName2.read()

