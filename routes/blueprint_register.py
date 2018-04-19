from flask import Blueprint


class Bp:
    blueprint_name_list = [
        "path",
        "get",
        "post",
    ]

    @staticmethod
    def generate_bp_list():
        for name in Bp.blueprint_name_list:
            setattr(Bp, name, Blueprint(name, __name__, template_folder='routes'))


Bp.generate_bp_list()

