#!/usr/bin/python3


"""
class_to_json
"""


def class_to_json(obj):
    """
    This returns the dictionary description with simple data structure
    (list, dictionary, string, integer and boolean) for JSON
    serialization of an object

    Arguments:
        obj {object} -- [The object to serialize]
    """

    return obj.__dict__
