#!/bin/bash

_LOGFILE=Main/core/logs/logs.txt
exec 6>&1
exec > $_LOGFILE

cd Main/logs
LOGFILE=logs.txt
exec 6>&1
exec > $LOGFILE
