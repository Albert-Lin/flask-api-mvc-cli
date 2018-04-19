from transformers import (SimpleDataTrans)
from .abstract_validator import AbstractValidator
from .required_validator import RequiredValidator
from flask import request


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
                }[method](kwargs, rules)

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
    def _post_validator(kwargs, rules):
        req_body = request.get_json(force=True)
        return Validator._validation_iterator(req_body, rules)

    @staticmethod
    def _get_validator(kwargs, rules):
        query_str_dict = dict(request.args)
        req_body = {}
        for key in query_str_dict:
            req_body[key] = query_str_dict[key][0]
        return Validator._validation_iterator(req_body, rules)

    @staticmethod
    def _path_param_validator(kwargs, rules):
        req_body = kwargs
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
            elif type(rules[key]) == dict:
                valid_result = {"code": 500, "message": "Request body structure error"}
            else:
                valid_result = Validator._column_validation(req_body, key, rules[key])

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
                rule_instance = rule
                valid_params = None
                if not isinstance(rule, AbstractValidator):
                    rule_instance = rule[0]
                    valid_params = rule[1]
                valid_result = Validator._general_validator(
                    rule_instance,
                    valid_params,
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
    def _general_validator(valid_instance, valid_params, req_body, key, nullable=False):
        # 01. initialize
        valid_fun = valid_instance.validator
        success = {"code": 200}
        # 02. column required validation
        required_result = Validator._required(req_body, key)
        # 03. input valid_fun validation
        if required_result["code"] == 200:
            if valid_fun(req_body, key, valid_params):
                return success
            else:
                return Validator._set_fail_response(valid_instance, key)
        else:
            if not nullable:
                return Validator._set_fail_response(valid_instance, key)
            else:
                return success

    @staticmethod
    def _required(req_body, key, nullable=True):
        required_validator = Validator._req
        valid_fun = required_validator.validator
        if valid_fun(req_body, key, None):
            return {"code": 200}
        else:
            return {"code": 500, "message": required_validator.message}

    @staticmethod
    def _set_fail_response(valid_instance, key):
        try:
            fail_response = {"code": 500, "message": valid_instance.message % key}
        except Exception as e:
            fail_response = {"code": 500, "message": valid_instance.message}
        return fail_response

