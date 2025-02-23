#!/usr/bin/python3

def uppercase(c):
    """Converts lowercase to uppercase"""
    newc = ''
    for i in c:
        if 97 <= ord(i) <= 122:
            letter = ord(i) - 32
            newc = newc + chr(letter)
        else:
            newc = newc + i
    print("{}".format(newc), end="")
    print("")
