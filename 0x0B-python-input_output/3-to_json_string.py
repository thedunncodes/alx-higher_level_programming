#!/usr/bin/python3


"""
to_json_string
"""


import json


def to_json_string(my_obj):
    """
    This returns the JSON representation of an object (string)

    Arguments:
        my_obj {object} -- [the object to be converted]
    """
    return json.dumps(my_obj)
