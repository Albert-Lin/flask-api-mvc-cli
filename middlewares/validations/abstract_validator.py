import abc


class AbstractValidator(metaclass=abc.ABCMeta):
    def __init__(self):
        self._default_error_message = None

    @abc.abstractmethod
    def validator(self, dict_data, key):
        return

    @property
    def info(self):
        return {
            "fun": self.validator,
            "message": self._default_error_message
        }
