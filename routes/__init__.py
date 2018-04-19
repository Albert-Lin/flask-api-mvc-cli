from utils import DynamicImporter
from routes.blueprint_register import Bp

DynamicImporter.package("routes")

all_blue_list = []
for name in Bp.blueprint_name_list:
    all_blue_list.append(getattr(Bp, name))

all_blue_list = tuple(all_blue_list)

