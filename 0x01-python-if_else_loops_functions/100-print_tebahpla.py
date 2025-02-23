#!/usr/bin/python3

upper = list(range(65, 91))
lower = list(range(97, 123))

upper = upper[::-1]
lower = lower[::-1]

for i in range(len(lower)):
    if i % 2 == 0:
        print("{}".format(chr(lower[i])), end="")
    else:
        print("{}".format(chr(upper[i])), end="")
