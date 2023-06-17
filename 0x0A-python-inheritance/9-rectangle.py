#!/usr/bin/python3


"""
A rectangle class that inherits from BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A rectangle class that inherits from BaseGeometry.
    """

    def __init__(self, width, height):
        """
        Initialize instance of the Rectangle class.

        Args:
        - width (int): width of the rectangle.
        - height (int): height of the rectangle.
        """

        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height

    def area(self):
        """
        This calculates the area of the rectangle.

        Returns:
        - Area of the rectangle.
        """

        return self.__width * self.__height

    def __str__(self):
        """
        This returns a string representation of the rectangle.

        Returns:
        A formatted string representing the rectangle.
        """

        return "[Rectangle] {}/{}".format(self.__width, self.__height)
