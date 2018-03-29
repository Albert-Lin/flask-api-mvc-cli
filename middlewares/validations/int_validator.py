from .abstract_validator import AbstractValidator


class IntegerValidator(AbstractValidator):
    def __init__(self):
        AbstractValidator.__init__(self)
        self._default_error_message = "column(%s) should be int!?"

    def validator(self, dict_data, key):
        value = dict_data[key]
        return type(value) == int


integer = IntegerValidator()




