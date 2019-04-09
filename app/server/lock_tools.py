import os

# this get our current location in the file system
import inspect
HERE_PATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

import time
import threading

# try catch so we can develop away from a RPI
try:

    import RPi.GPIO as GPIO

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    LED_PIN = 20
    GPIO.setup(LED_PIN, GPIO.OUT, initial=GPIO.LOW)

    LOCK_PIN = 21
    GPIO.setup(LOCK_PIN, GPIO.OUT, initial=GPIO.LOW)

    BUTTON_PIN = 26
    GPIO.setup(BUTTON_PIN, GPIO.IN)

    class Vault(threading.Thread):

        def __init__(self):
            threading.Thread.__init__(self)
            self.daemon = True
            self.interrupted = threading.Lock()

            self.unlock_timout_s = 10  # timeout for overheating lock security
            self.unlock_time = time.time() - self.unlock_timout_s  # to force a close event
            self.set_led_to_door_state()

            # add callback on door button
            GPIO.add_event_detect(BUTTON_PIN, GPIO.BOTH)
            GPIO.add_event_callback(BUTTON_PIN, self.door_state_change_callback)

            # start threah for lock security
            self.start()

        def run(self):
            self.interrupted.acquire()
            while self.interrupted.locked():
                # check time since lock is open (powered) to avoid overheating
                if (time.time() - self.unlock_time) > self.unlock_timout_s :
                    self.close_lock()
                time.sleep(0.1)

        def stop(self):
            self.interrupted.release()

        def door_state_change_callback(self, callback_info):
            time.sleep(1)  # sleep for better UI
            self.set_led_to_door_state()
            if self.is_door_open() and self.waiting_for_door_to_open :
                self.close_lock()

        def open_lock(self):
            GPIO.output(LOCK_PIN, GPIO.HIGH)
            self.waiting_for_door_to_open = True
            self.unlock_time = time.time()

        def close_lock(self):
            GPIO.output(LOCK_PIN, GPIO.LOW)
            self.waiting_for_door_to_open = False

        def is_door_open(self):
            return not bool(GPIO.input(BUTTON_PIN))

        def set_led_to_door_state(self):
            GPIO.output(LED_PIN, GPIO.input(BUTTON_PIN))

except:

    class Vault():

        def __init__(self):
            pass

        def open_lock():
            print('Opening Vault')

# create vault instance
vault = Vault()
