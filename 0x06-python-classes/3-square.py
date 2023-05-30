#!/usr/bin/python3

"""CLass square"""


class Square:
    """
    Class named square or class square

    Attributes:
        size (int): size of class square
    """
    def __init__(self, size=0):
        """
        Init method for Square
        Args:
            size: instance size
        Raises:
            TypeError: except if size is not an integer
            ValueError: except if size is less than 0
        """
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        def area(self):
            """
            this is a public instance method, returns curr sqr area
            """
            return self.__size ** 2
