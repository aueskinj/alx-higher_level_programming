#!/usr/bin/python3

data = [(1, 2), (3, 4), (5, 6)]
multiplication = [x*y for x, y in data]
add = [y for x,y in data]
print(multiplication)
print(sum(multiplication))
print(add)
print(sum(add))
print(sum(multiplication)/sum(add))
