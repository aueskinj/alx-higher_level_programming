#!/usr/bin/python3

def mystery_function(a, b):
    result = 0

    
    for i in range(1, 3):
        try:
            if i > a:
                raise Exception("Too far")
            result += (a ** b) / i
        except:
            result = a + b # This part is redundant in Python as `break` is inside `except`

    return result

