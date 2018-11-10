#!/bin/bash

# Create surveillance directories and download scripts
mkdir /home/pi/surveillance
mkdir /home/pi/surveillance/records
$ wget -O opencv_contrib.zip https://raw.githubusercontent.com/Xaxis/rpisurveillance/master/motion_detected.py

# Create custom Motion config directory and download config
mkdir /home/pi/.motion

