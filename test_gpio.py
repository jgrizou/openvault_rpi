import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.OUT)

for i in range(10):
	print(i)
	GPIO.output(27, GPIO.HIGH)
	time.sleep(1)
	GPIO.output(27, GPIO.LOW)
	time.sleep(1)
