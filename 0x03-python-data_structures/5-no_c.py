#!/usr/bin/python3

def no_c(my_string):
    new_string = ''
    for i in range(len(my_string)):
        if ord(my_string[i]) == 99  or ord(my_string[i]) == 67:
            continue
        new_string += my_string[i]
    return new_string
            
