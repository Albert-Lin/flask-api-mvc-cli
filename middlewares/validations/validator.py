from transformers import (SimpleDataTrans)
from .required_validator import RequiredValidator


class Validator:
    _req = RequiredValidator()

    def __init__(self):
        pass

    @staticmethod
    def validator(method=None, rules={}):
        def decorator(fun):
            def process(*args, **kwargs):
                valid_result = {
                    "post": Validator._post_validator,
                    "get": Validator._get_validator,
                    "path": Validator._path_param_validator,
                }[method](args, kwargs, rules)

                if valid_result["code"] == 200:
                    return fun(*args, **kwargs)
                else:
                    trans = SimpleDataTrans()
                    trans.status = 500
                    trans.message = valid_result["message"]
                    return trans.to_json()
            return process
        return decorator

    @staticmethod
    def _post_validator(args, kwargs, rules):
        req_body = kwargs["request"].get_json(force=True)
        return Validator._validation_iterator(req_body, rules)

    @staticmethod
    def _get_validator(args, kwargs, rules):
        query_str_dict = dict(kwargs["request"].args)
        req_body = {}
        for key in query_str_dict:
            req_body[key] = query_str_dict[key][0]
        return Validator._validation_iterator(req_body, rules)

    @staticmethod
    def _path_param_validator(args, kwargs, rules):
        req_body = {}
        for i in range(len(args)):
            if i > 0:
                req_body[i-1] = args[i]
        return Validator._validation_iterator(req_body, rules)

    @staticmethod
    def _validation_iterator(req_body, rules):
        valid_result = {"code": 200, "message": ""}
        for key in rules:
            if key in req_body:
                if type(rules[key]) == dict:
                    valid_result = Validator._validation_iterator(req_body[key], rules[key])
                else:
                    valid_result = Validator._column_validation(req_body, key, rules[key])
            else:
                valid_result = {"code": 500, "message": "Request body structure error"}

            if valid_result["code"] != 200:
                break

        return valid_result

    @staticmethod
    def _column_validation(req_body, key, column_rules):
        # 01. default result
        result = {"code": 200, "message": []}
        # 02. nullable check
        nullable = True
        for rule in column_rules:
            if type(rule) == RequiredValidator:
                nullable = False
                break
        # 03. iterator for each rule for column
        for rule in column_rules:
            try:
                # 04. invoke rule validator
                valid_fun_info = rule.info
                error_message = valid_fun_info["message"]
                valid_result = Validator._general_validator(
                    valid_fun_info["fun"],
                    error_message,
                    req_body,
                    key,
                    nullable=nullable
                )

                # 05. update result
                if valid_result["code"] != 200:
                    result["code"] = 500
                    result["message"].append(valid_result["message"])
            except Exception as e:
                pass
        return result

    @staticmethod
    def _general_validator(valid_fun, valid_message, req_body, key, nullable=False):
        # 01. initialize response
        success = {"code": 200}
        try:
            fail_response = {"code": 500, "message": valid_message % key}
        except Exception as e:
            fail_response = {"code": 500, "message": valid_message}

        # 02. column required validation
        required_result = Validator._required(req_body, key)
        # 03. input valid_fun validation
        if required_result["code"] == 200:
            if valid_fun(req_body, key):
                return success
            else:
                return fail_response
        else:
            if not nullable:
                return fail_response
            else:
                return success

    @staticmethod
    def _required(req_body, key, nullable=True):
        valid_info = Validator._req.info
        if valid_info["fun"](req_body, key):
            return {"code": 200}
        else:
            return {"code": 500, "message": valid_info["message"]}


