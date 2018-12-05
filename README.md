# rpi-motion-surveillance

## Summary

A basic Motion based Raspberry Pi Surveillance system.

I got tired of running the commands found in `install_rpi_surveillance.sh` whenever I setup a new Raspberry Pi
based surveillance system so I put this little project together to make things a little easier. This is a very basic configuration of [Motion](https://motion-project.github.io/motion_guide.html) 
but it may be great place for you to start if you're interested in building your own surveillance system.

### Requirements 

* A Raspberry Pi 3 to 3b+
* A Raspberry Pi compatible camera that is plugged in
* Python 3 installed (should be installed by default in Raspbian Jessie or Stretch)
* Script must be ran as the `pi` user

### Features

* An easy to use setup/installation script
* A motion detection script that sends you a message via email when motion is detected
* A script that removes the days recorded images and installs itself to crontab

### Getting started

1. Clone the repo into your home directory:  
`sudo git clone https://github.com/Xaxis/rpisurveillance.git`

2. Update the following lines in `motion_detected.py` to match your sending email
addresses credentials and your target email address.

    ```python
    sender = 'source@gmail.com'
    gmail_password = 'yourpassword!'
    recipients = ['target@gmail.com']
    ```

3. Run install the install script from within the `rpisurveillance` directory:  
`cd rpisurveillance`  
`chmod 777 install_rpi_surveillance.sh`  
`sudo ./install_rpi_surveillance.sh`

4. That's all! Your motion detection system should work after your next reboot.
If you want to test your setup before rebooting you can run:  
`sudo motion -s -c /home/.motion/motion.conf`

### Author

Wil Neeley ( [twitter](http://twitter.com/wilneeley) / [linkedin](https://www.linkedin.com/in/wil-neeley-87500852/) )
