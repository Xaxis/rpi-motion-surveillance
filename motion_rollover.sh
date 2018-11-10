#!/bin/bash
# Deletes all files recorded by Motion. Can be setup as a cronjob using crontab -e and adding the line:
# 0 0 * * * /home/pi/surveillance/motion_rollover.sh

sudo rm -rf /home/pi/surveillance/records/*