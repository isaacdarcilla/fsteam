#!/bin/bash
# Proper header for a Bash script.
# Cleaner
# reassign-stdout.sh
# Run as root
LOG_DIR=Main/core/logs
asul="\033[1;34m"
rescolor="\e[0m"
# Variables are better than hard-coded values.
echo "[+] Cleaning log files. Please wait."
sleep 2
rm -R Main/logs/*.txt
cd $LOG_DIR
rm -R *.txt
echo "[+] Logs cleaned up. No more rogue process."

exit # The right and proper method of "exiting" from a script.


