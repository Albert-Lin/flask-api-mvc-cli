from flask import Blueprint

path = Blueprint("path", __name__, template_folder='route')
get = Blueprint("get", __name__, template_folder='route')
post = Blueprint("post", __name__, template_folder='route')
