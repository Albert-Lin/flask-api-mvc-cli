import abc


class AbstractBaseTrans(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def to_dict(self):
        return

    @abc.abstractmethod
    def to_json(self, test=False):
        return

