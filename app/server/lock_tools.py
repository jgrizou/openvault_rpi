import os

# this get our current location in the file system
import inspect
HERE_PATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

import time

import RPi.GPIO as GPIO


LOCK_PIN = 21
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LOCK_PIN, GPIO.OUT)

def open_lock(duration_second=1):
	GPIO.output(LOCK_PIN, GPIO.HIGH)
	time.sleep(duration_second)
	GPIO.output(LOCK_PIN, GPIO.LOW)
