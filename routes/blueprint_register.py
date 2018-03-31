from flask import Blueprint

path = Blueprint("path", __name__, template_folder='routes')
get = Blueprint("get", __name__, template_folder='routes')
post = Blueprint("post", __name__, template_folder='routes')
