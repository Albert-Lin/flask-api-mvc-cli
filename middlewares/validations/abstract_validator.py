import abc


class AbstractValidator(metaclass=abc.ABCMeta):
    def __init__(self):
        self._default_error_message = None

    @abc.abstractmethod
    def validator(self, dict_data, key):
        """
        The main function of validation,
        it's for overriding.
        :param dict_data: a dict data
        :param key: key for dict_data
        :return: bool
        """
        return

    @property
    def info(self):
        """
        The validator info dict for using in
        'request_validator'
        :return: dict
        """
        return {
            "fun": self.validator,
            "message": self._default_error_message
        }
