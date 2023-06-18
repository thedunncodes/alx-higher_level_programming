#!/usr/bin/python3


"""
pascal_triangle
"""


def pascal_triangle(n):
    """
    This returns a list of lists of ints reping the Pascal’s triangle of n


    Arguments:
        n {int} -- [The size of triangle]

    Returns:
        list -- [The list of lists of integers reping Pascal's triangle of n]
    """

    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        row.append(1)
        triangle.append(row)
    return triangle
