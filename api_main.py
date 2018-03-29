from flask import Flask, request
from flask_cors import CORS
from configs import flask_config, flask_xss
import controllers as ctrl


app = Flask(__name__)
cors = CORS(app, resources=flask_xss)


@app.route("/api/<int:user_id>/<string:message>", methods=["GET"])
def path_param(user_id, message):
    """
    This is an example of api which passing
    data from URL
    :param user_id: an integer data
    :param message: an string data
    :return: JSON
    """
    return ctrl.example.path_param(user_id, message)


@app.route("/api/query-string", methods=["GET"])
def query_string():
    """
    This is an example of api which passing
    data by query string.
    *Note: The type of all data is "string"
    :return: JSON
    """
    return


@app.route("/api/post_json", methods=["POST"])
def post_json():
    """
    This is an example of api which passing
    JSON data from POST request body
    :return:
    """
    return


if __name__ == "__main__":
    app.run(host=flask_config['host'],
            port=flask_config['port'],
            debug=flask_config['debug'])

