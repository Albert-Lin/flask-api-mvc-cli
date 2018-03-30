import flask
import route.blueprint_register as register_list
from .example_route import *

all_blue_list = []
for item in dir(register_list):
    data = getattr(register_list, item)
    if type(data) == flask.blueprints.Blueprint:
        all_blue_list.append(data)

all_blue_list = tuple(all_blue_list)

