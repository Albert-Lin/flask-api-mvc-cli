from flask import request
import controllers as ctrl
from .blueprint_register import Bp
from middlewares import *


@Bp.path.route("/api/<int:user_id>/<string:message>", methods=["GET"])
@Valid.validator(method="path", rules={
    "user_id": [V.REQ, V.INT],
    "message": [V.REQ, V.STR],
})
def path_param(user_id, message):
    """
    This is an example of api which passing
    data from URL
    :param user_id: an integer data
    :param message: an string data
    :return: JSON
    """
    return ctrl.example.path_param(user_id, message)


@Bp.get.route("/api/query-string", methods=["GET"])
@Valid.validator(method="get", rules={
    "user_id": [V.REQ]
})
def query_string():
    """
    This is an example of api which passing
    data by query string.
    *Note: The type of all data is "string"
    :return: JSON
    """
    return ctrl.example.query_string(request)


@Bp.post.route("/api/post_json", methods=["POST"])
@Valid.validator(method="post", rules={
    "num0": [V.REQ, V.INT],
    "num1": [V.REQ, V.INT]
})
def post_json():
    """
    This is an example of api which passing
    JSON data from POST request body
    :return:
    """
    return ctrl.example.post_json(request)


