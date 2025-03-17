#!/usr/bin/python3
my_list = [1, 2, 3, 4, 5, "dg"]
for i in my_list:
    try:
        int(i)
        print(i)
    except (ValueError, TypeError):
        continue
