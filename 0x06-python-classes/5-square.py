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
        """
        self.__size = size

    @property
    def size(self):
        """
        this is a public instance method, returns curr sqr size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        this is a public instance method, returns curr sqr size
        Args:
            value: this is size of the square

        Raises:
            TypeError: except if size is not an integer
            ValueError: except if size is less than 0
        """
        if isinstance(value, int) is False:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        this is a public instance method, returns curr sqr area
        """
        return self.__size ** 2

    def my_print(self):
        """
        this is a public instance method, prints in stdout a square with char #
        """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print()
