#!/usr/bin/python3


"""
save_to_json_file
"""


import json


def save_to_json_file(my_obj, filename):
    """
    This writes an Object to a text file, using a JSON representation

    Arguments:
        my_obj {object} -- [The object to be converted]
        filename {str} -- [The name of the file]
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        json.dump(my_obj, f)
