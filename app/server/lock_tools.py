import os

# this get our current location in the file system
import inspect
HERE_PATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

import time

# try catch so we can develop away from a RPI
try:
    import RPi.GPIO as GPIO

    LOCK_PIN = 21
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(LOCK_PIN, GPIO.OUT)

    def open():
        GPIO.output(LOCK_PIN, GPIO.HIGH)

    def close():
        GPIO.output(LOCK_PIN, GPIO.LOW)

except:

    def open():
        print('Opening Vault')

    def close():
        print('Closing Vault')
