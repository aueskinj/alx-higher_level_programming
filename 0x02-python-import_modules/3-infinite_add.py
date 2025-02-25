#!/usr/bin/python3

import sys

if __name__ == "__main__":
    lis = []
    # number = [int(arg) for arg in sys.argv if arg.lstrip('-').isdigit()]:a list comprehension for the 
    # code below
    for i in range(1, len(sys.argv)):
        number = int(sys.argv[i])
        if sys.argv[i].lstrip('-').isdigit():
            lis.append(number)
        else:
            print("Error: Input is not a number")
    print("{}".format(sum(lis)))
