#!/usr/bin/python3
my_list = [1, 2, 3, 4, 5,]
list2 = [5, 4, 3, 2, 1]
for i,k in zip(my_list, list2):
    try:
        print(i, k)
    except (ValueError, TypeError):
        continue
