import os

# this get our current location in the file system
import inspect
HERE_PATH = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))


from flask import Flask, render_template
app = Flask(__name__)


from tools import SERVE_FOLDER
app = Flask(__name__, static_folder=SERVE_FOLDER, template_folder=SERVE_FOLDER, static_url_path='')


# when opening the root, we server index.html
@app.route('/')
def index():
    return render_template('index.html')

# if the page need to load files, this allow the server to server them for all urls
@app.route('/<path:path>')
def serve_static(path):
    return app.send_from_directory('', path)


if __name__ == '__main__':
    app.run()
