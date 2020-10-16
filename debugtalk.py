# -*- coding: UTF-8 -*-
from jsonschema import validate

def json_schema(json, schema):
    assert validate(instance=json, schema=schema) == None