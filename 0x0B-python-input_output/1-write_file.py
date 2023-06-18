#!/usr/bin/python3


"""
write_file
"""


def write_file(filename="", text=""):
    """
    A method for write_file.

    Args:
        filename (str): File name.
        text (str): The Text to write
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(text)
