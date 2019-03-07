import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

PIN = 27

GPIO.setup(PIN, GPIO.OUT)

for i in range(10):
	print(i)
	GPIO.output(PIN, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(PIN, GPIO.LOW)
	time.sleep(1)
