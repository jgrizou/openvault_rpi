
#dyndns

https://www.duckdns.org/
https://stackoverflow.com/questions/13322485/how-to-get-the-primary-ip-address-of-the-local-machine-on-linux-and-os-x

## script

> wlan_ip=$(ifconfig wlan0 | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1')

> echo url="https://www.duckdns.org/update?domains=openvault&token=81fd986d-1745-4f3f-99a0-6acbdded71c1&ip=$wlan_ip" | curl -k -o ~/duckdns/duck.log -K -



# ssh

https://www.raspberrypi.org/documentation/remote-access/ssh/


# miniconda 

https://gist.github.com/simoncos/a7ce35babeaf73f512be24135c0fbafb

## gpio

pip install rpi.gpio
