#!/usr/bin/python3

def islower(letter):
    """Scans each character in text.
Converts only lowercase letters (a-z) to uppercase (A-Z).
Leaves non-letter characters (digits, spaces, punctuation, etc.) unchanged.
Returns a new string."""

    for i in letter:
        if 97 <= ord(i) <=122:
            return True