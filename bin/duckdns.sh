#!/bin/bash

# free dynamic dns https://www.duckdns.org

# schedule this script with cron
# run in terminal: crontab -e
# add: */5 * * * * ~/workspace/openvault_rpi/bin/duckdns.sh > ~/workspace/openvault_rpi/logs/cron.log 2>&1


duckdns_log_file=/home/pi/workspace/openvault_rpi/logs/duckdns.log


printf "### CRON START ### \n\n"

# fetching wlan local ip
ip=$(/sbin/ifconfig wlan0 | grep -Eo 'inet (addr:)?([0-9]*\.){3}[0-9]*' | grep -Eo '([0-9]*\.){3}[0-9]*' | grep -v '127.0.0.1')

printf "IP = $ip \n\n"

printf "GET_REQUEST = https://www.duckdns.org/update?domains=openvault&token=81fd986d-1745-4f3f-99a0-6acbdded71c1&ip=$ip \n\n"

# sending to server
echo url="https://www.duckdns.org/update?domains=openvault&token=81fd986d-1745-4f3f-99a0-6acbdded71c1&ip=$ip" | curl -k -o $duckdns_log_file -K -

printf "\n### CRON STOP ###\n"
