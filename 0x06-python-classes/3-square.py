#!/usr/bin/python3

""Defines a class Square.""


class Square:
    """Represent a square."""

    def __init__(self, size=0):
        
        if not isinstance(size, int):
            raise TypeError("the size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        ""Return the current area of the square.""
        return (self.__size ** 2)
