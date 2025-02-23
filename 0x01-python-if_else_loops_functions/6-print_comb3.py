#!/usr/bin/python3

print(", ".join(
    "{}{}".format(d1, d2)
    for d1 in range(10) for d2 in range(d1 + 1, 10)
))
