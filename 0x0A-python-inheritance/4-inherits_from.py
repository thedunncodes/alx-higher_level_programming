#!/usr/bin/python3


"""
inherits_from
"""


def inherits_from(obj, a_class):
    """
    This checks if an object is an instance of a class that inherited from
    the specified class

    Args:
        obj (any): object to be checked
        a_class (any): class to be checked against

    Returns:
        bool: True,if the object is an instance of a class that inherited from
        the specified class
    """
    return isinstance(obj, a_class) and type(obj) != a_class
