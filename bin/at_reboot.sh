#!/bin/bash

chrome_log_file=/home/pi/workspace/openvault_rpi/logs/chrome.log
flask_log_file=/home/pi/workspace/openvault_rpi/logs/flask.log
url=https://jgrizou.com
url=http://127.0.0.1:5000/

## FLASK

echo "" >> $flask_log_file
echo "####################" >> $flask_log_file
echo "# NEW BOOT - $(date) #" >> $flask_log_file
echo "####################" >> $flask_log_file
echo "" >> $flask_log_file

source activate openvault_rpi

python /home/pi/workspace/openvault_rpi/app/server/app.py &>> $flask_log_file &


## CHROME

echo "" >> $chrome_log_file
echo "####################" >> $chrome_log_file
echo "# NEW BOOT - $(date) #" >> $chrome_log_file
echo "####################" >> $chrome_log_file
echo "" >> $chrome_log_file

DISPLAY=:0 /usr/bin/chromium-browser --no-first-run --noerrdialogs --start-fullscreen --disable-notifications --disbale-infobars --kiosk --app=$url &>> $chrome_log_file &
