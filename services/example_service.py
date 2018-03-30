class ExampleService:
    def __init__(self):
        pass

    def show_message(self, data):
        """
        An example function for ExampleController
        :param data: a dictionary data
        :return: str || bool
        """
        if "user_id" in data and "message" in data:
            return str(data["user_id"]) + " say: '" + data["message"] + "'."
        else:
            return False

    def sum(self, num0=None, num1=None):
        """
        An example function for ExampleController
        :param num0:
        :param num1:
        :return:
        """
        if num0 is None or num1 is None:
            return 0
        else:
            return num0 + num1
