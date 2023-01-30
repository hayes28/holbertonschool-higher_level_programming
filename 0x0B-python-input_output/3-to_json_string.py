#!/usr/bin/python3
""" returns the JSON representation of an object (string) """

import json


def to_json_string(my_obj):
    """Converts an object to JSON."""
    return json.dumps(my_obj)
