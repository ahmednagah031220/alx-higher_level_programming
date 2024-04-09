#!/usr/bin/python3
"""
Defining a class of rectangle
"""


class Rectangle:
    """rectangle adjustifying"""
    def __init__(self, width=0, height=0):
        """Intiation of the variables"""
        self.height = height
        self.width = width

    @property
    def width(self):
        """retrival of the value of the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of the width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """retrival of the value of the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter of the height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the perimeter of the rectangle"""
        if self.__height == 0 or self.__width == 0:
            return 0
        return 2 * (self.__height + self.__width)

    def __str__(self):
        """returning the visual shape of the rectangle using #"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width
                                for j in range(self.__height))
        return string
