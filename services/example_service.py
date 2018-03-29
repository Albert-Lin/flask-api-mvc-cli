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
