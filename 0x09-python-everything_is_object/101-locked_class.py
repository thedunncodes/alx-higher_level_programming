#!/usr/bin/python3

"""Locked CLass"""


class LockedClass:

    """A class that only lets the user to create the instance
       attribute 'first_name'"""
    __slots__ = ['first_name']
