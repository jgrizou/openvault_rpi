import os

# this get our current location in the file system
import inspect
HERE_PATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

import random

def random_boolean():
    return random.choice([True, False])

def random_text():
    return random.choice(['#', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])

import time
import numpy as np
import RPi.GPIO as GPIO

LOCK_PIN = 21
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(LOCK_PIN, GPIO.OUT)

def open_lock(duration_second=1):
	GPIO.output(LOCK_PIN, GPIO.HIGH)
	time.sleep(duration_second)
	GPIO.output(LOCK_PIN, GPIO.LOW)


from flask import Flask, render_template
from flask_socketio import SocketIO, emit

from tools import SERVE_FOLDER
app = Flask(__name__, static_folder=SERVE_FOLDER, template_folder=SERVE_FOLDER, static_url_path='')

app.config['SECRET_KEY'] = 'secret!'

socketio = SocketIO(app)


# when opening the root url, we server index.html that was compiled via npm in SERVE_FOLDER
@app.route('/')
def index():
    return render_template('index.html')

# if the page need to load files, this allow the server to server them for all urls
@app.route('/<path:path>')
def serve_static(path):
    return app.send_from_directory('', path)


@socketio.on('connect')
def on_connect():
    print('Clients connected')

@socketio.on('disconnect')
def on_disconnect():
    print('Clients disconnected')

@socketio.on('log')
def on_log(data):
    print(data)

@socketio.on('click')
def on_click(feedback_info):
    print(feedback_info)

    if random_boolean():
        emit('flash', np.random.randint(0, 2, 10, dtype="bool").tolist())
    else:
        emit('message', 'Test...')

    code_dict = []
    for _ in range(4):
        code_dict.append({'found': random_boolean(), 'ongoing': random_boolean(), 'text': random_text()})
    socketio.emit('code', code_dict)


if __name__ == '__main__':
    print('Flask is running in python')

    # import eventlet
    # import random
    #
    # def random_boolean():
    #     return random.choice([True, False])
    #
    # def random_text():
    #     return random.choice(['#', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'])
    #
    # ## from https://github.com/miguelgrinberg/python-socketio/issues/16
    # def background_emit():
    #     while True:
    #         code_dict = []
    #         for _ in range(4):
    #             code_dict.append({'found': random_boolean(), 'ongoing': random_boolean(), 'text': random_text()})
    #         socketio.emit('code', code_dict)
    #         eventlet.sleep(1)
    #
    # eventlet.monkey_patch(time=True)
    # eventlet.spawn(background_emit)

    socketio.run(app, host='0.0.0.0')
