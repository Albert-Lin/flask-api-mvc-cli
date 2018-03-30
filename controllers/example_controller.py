from transformers import SimpleDataTrans
from services import ex_service


class ExampleController:
    def __init__(self):
        pass

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

    def query_string(self, request):
        """
        01. Different from path_param, if the method of
        validation is "get", the key of rules should be
        parameter name

        02. Because all types of parameters value will be
        string, it is not necessary to add type rules
        (e.g., V.INT, V.STR)

        :param request: flask request
        :return: JSON
        """
        # 01. access data by request.args.get('{parameter_name}');
        user_id = request.args.get('user_id')
        num0 = request.args.get('num0')
        num1 = request.args.get('num1')

        try:
            # 02. invoke service
            result = ex_service.sum(int(num0), int(num1))

            # 03. transform and return response
            return SimpleDataTrans.success_json_response(result)
        except Exception as ex:
            trans = SimpleDataTrans()
            trans.message = str(ex)
            trans.status = 500
            return trans.to_json()

    def post_json(self, request):
        """
        01. In post validation, you might set customise
        rules for each column, even the nest columns
        :param request: flask request
        :return: JSON
        """
        request_body = request.get_json(force=True)
        num0 = request_body["num0"]
        num1 = request_body["num1"]

        result = ex_service.sum(num0, num1)

        return SimpleDataTrans.success_json_response(result*10)