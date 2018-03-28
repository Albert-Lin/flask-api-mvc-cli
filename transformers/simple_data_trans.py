from transformers import AbstractBaseTrans
from flask import jsonify


class SimpleDataTrans(AbstractBaseTrans):
    def __init__(self):
        super().__init__()
        self._data = []
        self._status = 200
        self._message = ""

    @property
    def data(self):
        return self._data

    @data.setter
    def data(self, data):
        self._data = data

    def append_data(self, data):
        self._data.append(data)

    @property
    def status(self):
        return self._status

    @status.setter
    def status(self, status):
        self._status = status

    @property
    def message(self):
        return self._message

    @message.setter
    def message(self, message):
        self._message = message

    def to_dict(self):
        return {
            "data": self._data,
            "status": self._status,
            "message": self._message
        }

    def to_json(self, test=False):
        if test:
            return self.to_dict()
        else:
            return jsonify(self.to_dict())

    @staticmethod
    def success_json_response(data=None):
        trans = SimpleDataTrans()
        if data is not None:
            trans.data = data
        return trans.to_json()

