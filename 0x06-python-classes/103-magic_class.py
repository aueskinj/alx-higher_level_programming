#!/usr/bin/python3
"""Module for the MagicClass class.

This module defines a MagicClass class that represents a circle with a radius.
"""

import math

class MagicClass:
    """A class that defines a circle by its radius.

    The radius is a private instance attribute. We validate that the radius
    is a number (int or float) when it's set.
    """

    def __init__(self, radius=0):
        """Initialize a new MagicClass instance.

        Args:
            radius: The radius of the circle (must be a number, either int or float).
        """
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")

        self.__radius = radius

    def area(self):
        """Returns the current area of the circle."""
        return math.pi * self.__radius ** 2

    def circumference(self):
        """Returns the current circumference of the circle."""
        return 2 * math.pi * self.__radius

    @property
    def radius(self):
        """Getter for radius."""
        return self.__radius

    @radius.setter
    def radius(self, value):
        """Setter for radius. Ensures it's a valid number."""
        if not isinstance(value, (int, float)):
            raise TypeError("radius must be a number")
        self.__radius = value
