# -*- coding: UTF-8 -*-
from jsonschema import validate
from jsonschema import ValidationError

def json_schema(json, schema):
    try:
        validate(instance=json, schema=schema)
    except ValidationError:
        raise AssertionError("Bad json")