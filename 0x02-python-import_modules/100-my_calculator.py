#!/usr/bin/python3
import sys

def main():
    
    if len(sys.argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a, operator, b = sys.argv[1], sys.argv[2], sys.argv[3]

    if not (a.isdigit() and b.isdigit()):
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)

    a, b = int(a), int(b)
    operations = {"+": add, "-": sub, "*": mul, "/": div}

    if operator in operations:
        ans = operations[operator](a, b)
        print("{} {} {} = {}".format(a, operator, b, ans))
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        sys.exit(1)

if __name__ == "__main__":
    from calculator_1 import *
    main()