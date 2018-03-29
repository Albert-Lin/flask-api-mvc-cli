from .validator import (Validator as Valid)
from .required_validator import RequiredValidator
from .int_validator import IntegerValidator
from .string_validator import StringValidator


class V:
    REQ = RequiredValidator()
    INT = IntegerValidator()
    STR = StringValidator()