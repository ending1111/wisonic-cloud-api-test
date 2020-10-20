# -*- coding: UTF-8 -*-
from jsonschema import validate
from jsonschema import ValidationError
from httprunner.exceptions import ValidationFailure

def json_schema(json, schema):
    try:
        validate(instance=json, schema=schema)
    except ValidationError as e:
        raise ValidationFailure("Bad json") from e