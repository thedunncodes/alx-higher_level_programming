#!/usr/bin/python3

"""CLass square"""


class Square:
    """
    Class named square or class square

    Attributes:
        size (int): size of class square
    """
    def __init__(self, size=0, position=(0, 0)):
        """This creates new instances of square

        Args:
            __size (int): the size of the class square (1 side)
            __position (tuple): The position of square
        """
        self.size = size
        self.position = position

    def area(self):
        """
        this is a public instance method, returns curr sqr area
        """
        return self.__size ** 2

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

    @property
    def position(self):
        """This returns position of square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """A property setter which returns position of square

        Args:
            value (tuple): the position of square.

        Raises:
            TypeError: If not 2 positive integers.
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")

        x, y = value
        if not isinstance(x, int) or not isinstance(y, int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if x < 0 or y < 0:
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def my_print(self):
        """
        A Public instance method which prints in stdout, sqr with char #
        and also a position for the sqr
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """A representation of square with '#'

        Returns:
            str: # square.
        """
        if self.__size == 0:
            return ''

        offset_lines = '\n' * self.position[1]
        offset_spaces = ' ' * self.position[0]
        line = offset_spaces + '#' * self.size
        square = '\n'.join(line for _ in range(self.size))

        return offset_lines + square
