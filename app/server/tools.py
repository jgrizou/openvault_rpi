import os

# this get our current location in the file system
import inspect
HERE_PATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

import json

# say the server where to serve the static files
SERVE_FOLDER=os.path.normpath(os.path.join(HERE_PATH, '../client/dist'))
CONFIG_FOLDER = os.path.join(HERE_PATH, 'configs')

def read_config(config_filename):
    with open(config_filename) as f:
        config = json.load(f)
    return config
