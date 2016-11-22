#!/bin/bash

sudo airmon-ng stop wlan0mon
sudo systemctl start NetworkManager.service
