#!/usr/bin/python3


"""
BaseGeometry update

2nd update with integer validator

"""


class BaseGeometry:
    """
    This BaseGeometry class defines the basic structure for geometric calc,
    this is updated to raise exception

    Methods:
    - area(): To raise an exception and be implemented in derived classes.
    """
    pass

    def area(self):
        """
        This calculates the area of the geometric shape.

        This method is intended to be overridden by derived classes to
        provide the specific implementation for calculating the area of
        the corresponding geometric shape.

        Raises:
        Exception: An exception is raised when called.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        This validates the value passed to the method.

        Args:
        - name (str): Name of variable to validate.
        - value (int): value to validate.

        Raises:
        TypeError: If the value is not an integer.
        ValueError: If the value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
