#!/usr/bin/python3
"""Module for the Square class.

This module defines a Square class that represents a square
with a private size attribute. No type or value verification is done.
"""


class Square:
    """A class that defines a square by its size.

    The size is a private instance attribute.
    """

    def __init__(self, size):
        """Initialize a new Square instance.

        Args:
            size: The size of the square (no type/value verification).
        """
        self.__size = size
