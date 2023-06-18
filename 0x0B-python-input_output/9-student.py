#!/usr/bin/python3


"""
Student class
"""


class Student:
    """
    A Student class.
    """

    def __init__(self, first_name, last_name, age):
        """
        This Initializes instance of Student class.

        Args:
            first_name (str): The first name of student
            last_name (str): The last name of student
            age (int): The age of student
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        This retrieves the dictionary representation of Student instance

        Returns:
            dict: The dictionary representation of Student instance
        """

        return self.__dict__
