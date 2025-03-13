#!/usr/bin/python3

"""
Prototype: def safe_print_list(my_list=[], x=0):
my_list can contain any type (integer, string, etc.)
All elements must be printed on the same line followed by a new line.
x represents the number of elements to print
x can be bigger than the length of my_list
Returns the real number of elements printed
You have to use try: / except:
You are not allowed to import any module
You are not allowed to use len()
"""
def safe_print_list(my_list=[], x=0):
    count = 0
    for i in range(x):
        try:
            print("{}".format(my_list[i]), end = "")
            count += 1
        except IndexError:
            break
    print()
    return (count)

if __name__ == "__main__":
    safe_print_list = __import__('0-safe_print_list').safe_print_list

    my_list = [1, 2, 3, 4, 5]

    nb_print = safe_print_list(my_list, 2)
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list(my_list, len(my_list))
    print("nb_print: {:d}".format(nb_print))
    nb_print = safe_print_list(my_list, len(my_list) + 2)
    print("nb_print: {:d}".format(nb_print))

# data = [42, "hello", 3.14, True, "Python", -7]
# x =20
# i = 0
# for i in range(x):
#     try:
           
# print(i)