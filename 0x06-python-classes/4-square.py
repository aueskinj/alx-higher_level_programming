#!/usr/bin/python3
"""Module for the Square class.

This module defines a Square class that represents a square
with a private size attribute. No type or value verification is done.
"""

class Square:
    """A class that defines a square by its size.

    The size is a private instance attribute.
    """

    def __init__(self, size=0):
        """Initialize a new Square instance.

        Args:
            size: The size of the square (with type and value verification).
        """
        self.__size = size

    def area(self):
        """Returns the current square area"""
        return ((self.__size)**2)
    
    @property
    def size(self):
        """Getter for Size"""
        return self.__size
    
    @size.setter
    def size(self, value):
        """Setter for size. Checks that the value is a positive integer"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

