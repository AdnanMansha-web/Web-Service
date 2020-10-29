#
# a flask webserver which provides the REST API for TUC DriveCloud
#

from pyapp import config

from flask import Flask, send_from_directory
from flask_restx import Resource, Api
import bcrypt

from pyapp.api import blueprint as rest_api

app = Flask(__name__)
app.register_blueprint(rest_api)

# instantiate the app
if config.DEBUG:
    from flask_cors import CORS
    print("Enabling CORS")
    # enable cross-origin resource sharing only for development
    CORS(app, expose_headers='Authorization')


@app.after_request
def add_header(r):
    # disable caching of API calls
    r.headers["Cache-Control"] = "no-store"    
    return r

@app.route('/files/<name>')
def serve_static(name):
    if config.DEBUG:
        return send_from_directory(config.DISK_CACHE_FOLDER, name)
    else:        
        return 400, "In production mode files should be served by the webserver directly"

if __name__ == '__main__':
    print("Starting server")
    app.run(host=config.STANDALONE_HOST, port=config.STANDALONE_PORT, debug=config.DEBUG)
