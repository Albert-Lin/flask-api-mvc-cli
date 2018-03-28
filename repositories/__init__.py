from mongoengine import *
from configs import mongodb_config as config
from .repository_factory import repository_factory
from models import *

sol_data = config["Sol-Data"]

connect(
    db=sol_data["db"],
    host=sol_data["host"],
    port=sol_data["port"],
    username=sol_data["username"],
    password=sol_data["password"]
)


