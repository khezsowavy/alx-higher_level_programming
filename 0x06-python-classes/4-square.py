#!/usr/bin/python3

"""Defines a class Square."""


class Square:
    """Represenst a square."""

    def __init__(self, size=0):
        """Initializes a new square.

        Args:
            size (int): The size of the new square.
        """
        self.size = size

    @property
    def size(self):
        """Get/set the current size of the square."""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError
        elif value < 0:
            raise ValueError
        self.__size = value

    def area(self):
        return (self.__size * self.__size)
