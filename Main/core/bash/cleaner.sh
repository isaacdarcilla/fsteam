#!/bin/bash
# Proper header for a Bash script.
# Cleaner
# Run as root
LOG_DIR=/Main/logs
asul="\033[1;34m"
rescolor="\e[0m"
# Variables are better than hard-coded values.
cd $LOG_DIR
rm *.txt
cat /dev/null > messages
cat /dev/null > wtmp

echo -e "\e[1;34m[+] Logs cleaned up. No more rogue process."$rescolor""
exit # The right and proper method of "exiting" from a script.


