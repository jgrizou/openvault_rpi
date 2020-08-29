# Procedure on RPI4

// enable ssh
sudo systemctl enable ssh
sudo systemctl start ssh

// install conda
wget https://github.com/jjhelmus/berryconda/releases/download/v2.0.0/Berryconda3-2.0.0-Linux-armv7l.sh
chmod +x Berryconda3-2.0.0-Linux-armv7l.sh
./Berryconda3-2.0.0-Linux-armv7l.sh

// pull repo
mkdir workspace
git clone https://github.com/jgrizou/openvault.git
git clone https://github.com/jgrizou/openvault_rpi.git

// instal dependencies
cd openvault_rpi
conda env create -f environment.yml

// activate the openvault_rpi env!!!!
source /home/pi/berryconda3/bin/activate openvault_rpi


conda install scipy
conda install scikit-learn

pip install flask
pip install flask-socketio
pip install eventlet
pip install gunicorn

pip install tinydb
pip install rpi.gpio

// sudo reboot

// compile client side
cd openvault_rpi/app/client
npm update
npm install
npm run build


# Script to run at startup

See bin/at_reboot.sh

Found at: https://askubuntu.com/questions/228304/how-do-i-run-a-script-at-start-up


# Dynamic DNS

See bin/duckdns.sh

Info:
- https://www.duckdns.org/
- https://stackoverflow.com/questions/13322485/how-to-get-the-primary-ip-address-of-the-local-machine-on-linux-and-os-x

# Wifi Pro @ CRI

> sudo apt-get install network-manager-gnome

- Make sure /etc/network/interface is default
- Make sure /etc/wpa_supplicant/wpa_supplicant.conf does not exist
- Use interface to configure as per CRI website: https://cri-paris.freshservice.com/support/solutions/articles/10000001839-how-can-i-access-the-wifi-

Force wifi to activate
- sudo rfkill unblock 0  ## 0 is the Wireless LAN, check with rfkill list
- sudo ifconfig wlan0 up  ## enable wlan0
- sudo nmcli radio wifi on  ## network manager enable wifi


# Enable SSH

https://www.raspberrypi.org/documentation/remote-access/ssh/

# Screen

Hardware: https://www.instructables.com/id/Raspberry-Pi-Touchscreen-Setup/

Screen config: in /etc/lightdm/lightdm.conf

no sleep: xserver-command=X -s 0 dpms
https://raspberry-projects.com/pi/pi-operating-systems/raspbian/gui/disable-screen-sleep

no cursor: xserver-command = X -nocursor
https://raspberrypi.stackexchange.com/questions/53127/how-to-permanently-hide-mouse-pointer-or-cursor-on-raspberry-pi


## Kiosk mode

Launch chrome from command line: DISPLAY=:0 chromium-browser

See bin/at_reboot.sh for all options

http://www.knight-of-pi.org/update-autostart-chromium-for-full-screen-applications/

https://stackoverflow.com/questions/22999829/disable-chrome-pinch-zoom-for-use-in-kiosk


## I2C sound

https://learn.adafruit.com/adafruit-max98357-i2s-class-d-mono-amp/

# Packages

## Python

Use berryconda: https://github.com/jjhelmus/berryconda

Load from requirements in environment.yml

To save the environment use script in bin/save_conda_environment.sh

To create from the environment.yml file:
> conda env create -f environment.yml


### some lib used

- conda install -c conda-forge nodejs
- conda install numpy
- pip install flask
- pip install flask-socketio
- pip install eventlet
- pip install tinydb

### rpi gpio

pip install rpi.gpio


## Web

npm
