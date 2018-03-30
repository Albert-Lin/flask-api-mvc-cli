from flask import Flask
from flask_cors import CORS
from configs import flask_config, flask_xss
from route import all_blue_list

app = Flask(__name__)
cors = CORS(app, resources=flask_xss)

for blue in all_blue_list:
    app.register_blueprint(blue)


if __name__ == "__main__":
    app.run(host=flask_config['host'],
            port=flask_config['port'],
            debug=flask_config['debug'])

