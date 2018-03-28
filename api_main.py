from flask import Flask, request
from flask_cors import CORS
from .configs import flask_config, flask_xss
from .controllers import Ctrl


app = Flask(__name__)
cors = CORS(app, resources=flask_xss)


if __name__ == "__main__":
    app.run(host=flask_config['host'],
            port=flask_config['port'],
            debug=flask_config['debug'])

