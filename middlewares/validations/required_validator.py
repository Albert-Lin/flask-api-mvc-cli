from .abstract_validator import AbstractValidator


class RequiredValidator(AbstractValidator):
    def __init__(self):
        AbstractValidator.__init__(self)
        self._default_error_message = "column(%s) is required"

    def validator(self, dict_data, key):
        return dict_data is not None and key in dict_data


