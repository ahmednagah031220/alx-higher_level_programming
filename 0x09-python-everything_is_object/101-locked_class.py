#!/usr/bin/python3
"""Define a locked class"""


class LockedClass:
    """
    Prevents any variable to be added in the class
    """
    __slots__ = ("first_name")
