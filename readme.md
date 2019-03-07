
#dyndns

https://www.duckdns.org/
https://stackoverflow.com/questions/13322485/how-to-get-the-primary-ip-address-of-the-local-machine-on-linux-and-os-x

## schedule
crontab -e
 > \*/5 * * * * ~/duckdns/duck.sh > ~/duckdns/cron.log 2>&1

## script

```
echo "CRON START"

# fetching wlan local ip
wlan_ip=$(/sbin/ifconfig wlan0 | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1')

echo "$wlan_ip"
echo url="https://www.duckdns.org/update?domains=openvault&token=81fd986d-1745-4f3f-99a0-6acbdded71c1&ip=$wlan_ip"

# sending to server
echo url="https://www.duckdns.org/update?domains=openvault&token=81fd986d-1745-4f3f-99a0-6acbdded71c1&ip=$wlan_ip" | curl -k -o ~/duckdns/duck.log -K -

echo "CRON STOP"
```

# Wifi Pro CRI

> sudo apt-get install network-manager-gnome

make sure /etc/network/interface is default
make sure /etc/wpa_supplicant/wpa_supplicant.conf does not exist

use interface to configure as per CRI website: https://cri-paris.freshservice.com/support/solutions/articles/10000001839-how-can-i-access-the-wifi-


# ssh

https://www.raspberrypi.org/documentation/remote-access/ssh/


# miniconda

https://gist.github.com/simoncos/a7ce35babeaf73f512be24135c0fbafb

## gpio

pip install rpi.gpio

# Screen

https://www.instructables.com/id/Raspberry-Pi-Touchscreen-Setup/

In /etc/lightdm/lightdm.conf

no sleep: xserver-command=X -s 0 dpms
https://raspberry-projects.com/pi/pi-operating-systems/raspbian/gui/disable-screen-sleep

no cursor: xserver-command = X -nocursor
https://raspberrypi.stackexchange.com/questions/53127/how-to-permanently-hide-mouse-pointer-or-cursor-on-raspberry-pi


## Kiosk

launch Chrome from command line: DISPLAY=:0 chromium-browser

http://www.knight-of-pi.org/update-autostart-chromium-for-full-screen-applications/

DISPLAY=:0 /usr/bin/chromium-browser --no-first-run --noerrdialogs --start-fullscreen --disable-notifications --disbale-infobars --kiosk https://jgrizou.co

## Schedule at startup

crontab -e

@reboot /home/pi/workspace/openvault_rpi/bin/at_reboot.sh

found at: https://askubuntu.com/questions/228304/how-do-i-run-a-script-at-start-up
