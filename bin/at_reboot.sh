#!/bin/bash

# schedule this script with cron
# run in terminal: crontab -e
# add: @reboot ~/workspace/openvault_rpi/bin/at_reboot.sh

## Enable Wifi

sudo rfkill unblock 0 # 0 is the Wireless LAN, check with rfkill list
sudo ifconfig wlan0 up
sudo nmcli radio wifi on ## network manager enable wifi

## Parameters

chrome_log_file="/home/pi/workspace/openvault_rpi/logs/chrome.log"
flask_log_file="/home/pi/workspace/openvault_rpi/logs/flask.log"

# url="http://127.0.0.1:5000/" # when served via flask
# url="http://127.0.0.1:1234/" # when served via npm run dev
# url="http://127.0.0.1:5000/#/ui/demo_level_3.json"
# url="http://127.0.0.1:5000/#/ui/level_5.json"
url="http://127.0.0.1:5000/#/ui/event_level_3_mcam.json"


## FLASK

echo "" >> $flask_log_file
echo "####################" >> $flask_log_file
echo "# NEW BOOT - $(date) #" >> $flask_log_file
echo "####################" >> $flask_log_file
echo "" >> $flask_log_file

echo "Activating openvault_rpi environment..." >> $flask_log_file
source /home/pi/berryconda3/bin/activate openvault_rpi &>> $flask_log_file

echo "Launching Flask server " >> $flask_log_file
# python -u option needed to remove buffer stdout from python
# see https://unix.stackexchange.com/questions/182537/write-python-stdout-to-file-immediately

# python -u /home/pi/workspace/openvault_rpi/app/server/app.py &>> $flask_log_file &

cd /home/pi/workspace/openvault_rpi/app/server
gunicorn -b localhost:5000 --worker-class eventlet -w 1 app:app &>> $flask_log_file &


## CHROME

echo "" >> $chrome_log_file
echo "####################" >> $chrome_log_file
echo "# NEW BOOT - $(date) #" >> $chrome_log_file
echo "####################" >> $chrome_log_file
echo "" >> $chrome_log_file

DISPLAY=:0 /usr/bin/chromium-browser --no-first-run --noerrdialogs --start-fullscreen --disable-notifications --disbale-infobars --disable-pinch --overscroll-history-navigation=0 --kiosk --app=$url &>> $chrome_log_file &

# Visual DEBUG
# DISPLAY=:0 /usr/bin/chromium-browser $url &>> $chrome_log_file &
