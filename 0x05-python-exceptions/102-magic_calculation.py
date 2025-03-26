#!/usr/bin/python3

def mystery_function(a, b):
    result = 0

    try:
        for i in range(1, 3):
            if i > a:
                raise Exception("Too far")
            result += (a ** b) / i
    except:
        result = a + b
        break  # This part is redundant in Python as `break` is inside `except`

    return result

