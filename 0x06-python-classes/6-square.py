#!/usr/bin/python3
"""Module for the Square class.

This module defines a Square class that represents a square
with a private size attribute. No type or value verification is done.
"""

class Square:
    """A class that defines a square by its size.

    The size is a private instance attribute.
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new Square instance.

        Args:
            size: The size of the square (with type and value verification).
            position: The position of the square, represented as a tuple of two integers.
        """
        self.size = size  # Use the setter for validation
        self.position = position  # Use the setter for validation

    def area(self):
        """Returns the current square area."""
        return self.size ** 2
    
    @property
    def size(self):
        """Getter for Size."""
        return self.__size
    
    @size.setter
    def size(self, value):
        """Setter for size. Checks that the value is a positive integer."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value
    
    @property
    def position(self):
        """Getter for position."""
        return self.__position

    @position.setter
    def position(self, value):
        """Setter for position. Checks the validity of the position and updates it."""
        # Validate that pos is a tuple of two positive integers.
        if (not isinstance(value, tuple) or
            len(value) != 2 or
            not all(isinstance(num, int) and num >= 0 for num in value)):
                raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value  # Set the position after validation
    
    def my_print(self):
        """Print in stdout the square with the character #."""
        if self.size == 0:
            print("")  # Print a blank line if size is 0
        else:
            for _ in range(self.position[1]):
                print("")  # Print the vertical spaces

            for _ in range(self.size):
                print(" " * self.position[0] + "#" * self.size)  # Print the square
