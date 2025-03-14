'''Write a function that creates a copy of the string, removing the character at the position n 
(not the Python way, the “C array index”).

Prototype: def remove_char_at(str, n):
You are not allowed to import any module'''

def remove_char_at(str, n):
    '''get's rid of the character at the position n'''
    return str[:n] + str[n+1:]