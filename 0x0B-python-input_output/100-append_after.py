#!/usr/bin/python3


"""
append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """
    This inserts a line of text to a file, after each line
    containing a specific string

    Arguments:
        filename {str} -- [The name of file]
        search_string {str} -- [The string to search for]
        new_string {str} -- [The string to insert]
    """

    with open(filename, 'r+') as f:
        lines = f.readlines()
        new_lines = []
        for line in lines:
            new_lines.append(line)
            if search_string in line:
                new_lines.append(new_string)
        f.seek(0)
        f.writelines(new_lines)
