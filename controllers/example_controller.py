from middlewares import *
from transformers import SimpleDataTrans
from services import ex_service


class ExampleController:
    def __init__(self):
        pass

    @Valid.validator(method="path", rules={
        0: [V.REQ, V.INT],
        1: [V.REQ, V.STR],
    })
    def path_param(self, user_id, message):
        """
        01. The keys of rules is index of *arg of
        function, e.g., 0 equals to user_id and
        1 equals to message

        02. In validator, all the parameters are from
        URL and the type is been define, so it is not
        necessary to add V.REQ and other type rules
        (e.g., V.INT, V.STR)

        03. The JSON response could be set simple with
        SimpleDataTrans

        :param user_id: integer data from api URL
        :param message: string data from api URL
        :return:
        """
        # invoke service for core business logic and
        # computed
        service_result = ex_service.show_message({
            "user_id": user_id,
            "message": message
        })

        # transformer
        if service_result:
            # There are two ways to create a JSON response
            # 01. complete: you can set data, status and message
            # three information completely
            response = SimpleDataTrans()
            response.data = service_result
            response.status = 0
            response.message = "api success"
            json = response.to_json()

            # 02. simple: using static method "success_json_response"
            # can generate a JSON response directly, the arg of
            # function for setting data information, status default as
            # 200 and message default as ""
            SimpleDataTrans.success_json_response(service_result)

            return json
        elif not service_result:
            response = SimpleDataTrans()
            response.status = 500
            response.message = "api 'path_param' is fail"
            return response.to_json()
