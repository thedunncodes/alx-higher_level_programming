#!/usr/bin/python3


"""
load_from_json_file
"""


import json


def load_from_json_file(filename):
    """
    This creates an Object from a “JSON file”

    Arguments:
        filename {str} -- [the name of the file]

    Returns:
        [object] -- [The object from a “JSON file”]
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
