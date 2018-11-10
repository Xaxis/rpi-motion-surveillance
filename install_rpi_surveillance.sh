#!/bin/bash

# Create surveillance directories and files
mkdir /home/pi/surveillance
echo "Created directory /home/pi/surveillance"
mkdir /home/pi/surveillance/records
echo "Created directory /home/pi/surveillance/records"
mkdir /home/pi/.motion
echo "Created directory /home/pi/.motion"
cp motion_detected.py /home/pi/surveillance/motion_detected.py
echo "Copied motion_detected.py to /home/pi/surveillance/motion_detected.py"
cp motion_rollover.sh /home/pi/surveillance/motion_rollover.sh
echo "Copied motion_rollover.sh to /home/pi/surveillance/motion_rollover.sh"
cp motion_startup.sh /home/pi/surveillance/motion_startup.sh
echo "Copied motion_startup.sh to /home/pi/surveillance/motion_startup.sh"
cp motion.conf /home/pi/.motion/motion.conf
echo "Copied motion.conf to /home/pi/.motion/motion_conf.sh"

# Install Motion
sudo apt-get install motion
echo "Installed motion via sudo apt-get install motion"

# Add motion to rc.local to run motion_startup.sh on boot
sudo sed -i 's|exit 0|# Start Motion on boot\nsudo bash /home/pi/surveillance/motion_startup.sh\n\nexit 0|' /etc/rc.local
echo "Added motion_startup.sh script to /etc/rc.local so as to run on boot."

# Install motion_rollover.sh as cron job to run every day at midnight
cronjob="\n# Run motion surveillance records script every day at midnight\n0 0 * * * /home/pi/surveillance/motion_rollover.sh"
(crontab -u pi -l; echo -e "$cronjob" ) | crontab -u pi -
echo "Installed motion_rollover.sh as cron job to run every day at midnight."
