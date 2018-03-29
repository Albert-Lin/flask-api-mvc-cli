from .abstract_validator import AbstractValidator


class StringValidator(AbstractValidator):
    def __init__(self):
        AbstractValidator.__init__(self)
        self._default_error_message = "column(%s) should be str!"

    def validator(self, dict_data, key):
        value = dict_data[key]
        return type(value) == str


string = StringValidator()
