#!/usr/bin/python3
"""
This module defines a singly linked list and allows insertion
of integers in sorted (ascending) order using the sorted_insert method.
"""

class Node:
    """
    Represents a node in a singly linked list.

    Each node holds an integer value and a reference to the next node.
    """

    def __init__(self, data, next_node=None):
        """
        Initialize a new Node instance.

        Args:
            data (int): The data to store in the node.
            next_node (Node): The next node in the list. Defaults to None.

        Raises:
            TypeError: If data is not an integer.
            TypeError: If next_node is not a Node instance or None.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get the value of the node's data."""
        return self.__data

    @data.setter
    def data(self, value):
        """Set the value of the node's data with validation."""
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get the next node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set the next node with validation."""
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """
    Represents a singly linked list with nodes sorted in ascending order.
    """

    def __init__(self):
        """
        Initialize an empty singly linked list.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Insert a new Node with the given value into the correct
        sorted position in the list.

        Args:
            value (int): The value to insert.
        """
        new_node = Node(value)
        if self.__head is None or self.__head.data > value:
            new_node.next_node = self.__head
            self.__head = new_node
        else:
            current = self.__head
            while current.next_node and current.next_node.data < value:
                current = current.next_node
            new_node.next_node = current.next_node
            current.next_node = new_node

    def __str__(self):
        """
        Return the string representation of the list,
        where each data value is printed on a new line.

        Returns:
            str: Newline-separated list of node values.
        """
        result = []
        current = self.__head
        while current:
            result.append(str(current.data))
            current = current.next_node
        return "\n".join(result)
