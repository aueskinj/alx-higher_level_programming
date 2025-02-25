#!/usr/bin/python3

import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("0 arguments.")

    elif(len(sys.argv) == 2):
        print("{} argument:".format(len(sys.argv[1:])))
        print("1 : {}".format(sys.argv[1]))
    elif(len(sys.argv) > 2):
        print("{} arguments:".format(len(sys.argv)))
        for index, arg in enumerate(sys.argv[1:], start = 1):
            print("{} : {}".format(index, arg))  
    