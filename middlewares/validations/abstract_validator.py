import abc


class AbstractValidator(metaclass=abc.ABCMeta):
    def __init__(self):
        self._default_error_message = None

    @abc.abstractmethod
    def validator(self, dict_data, key, params):
        return

    @property
    def message(self):
        return self._default_error_message
