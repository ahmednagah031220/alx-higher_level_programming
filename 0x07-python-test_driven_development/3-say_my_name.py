#!/usr/bin/python3
"""
find out the name of the user
"""
def say_my_name(first_name, last_name=""):
    """
    Prints the first and the last name of the user

    Args:
        first_name: the first name
        last_name: the last name
    """

    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
