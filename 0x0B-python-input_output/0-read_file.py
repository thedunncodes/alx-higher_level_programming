#!/usr/bin/python3


"""
read_file
"""


def read_file(filename=""):
    """
    A method for read_file.

    Args:
        filename (str): file name.
    """
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
