import os

# this get our current location in the file system
import inspect
HERE_PATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))

# say the server where to serve the static files
SERVE_FOLDER=os.path.normpath(os.path.join(HERE_PATH, '../client/dist'))
