#!/usr/bin/python3


"""
from_json_string
"""


import json


def from_json_string(my_str):
    """
    This returns an object (Python data structure) represented by a JSON string

    Arguments:
        my_str {str} -- [The string to be converted]
    """
    return json.loads(my_str)
