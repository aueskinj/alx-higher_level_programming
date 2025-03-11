#!/usr/bin/python3

def weight_average(my_list=[]):
    data = [(1, 2), (3, 4), (5, 6)]
    weighted, weights= [x*y for x, y in my_list], [y for x,y in my_list]
    return (sum(weighted)/sum(weights))

if __name__ == "__main__":
    weight_average = __import__('100-weight_average').weight_average

    my_list = [(1, 2), (2, 1), (3, 10), (4, 2)]
    # = ((1 * 2) + (2 * 1) + (3 * 10) + (4 * 2)) / (2 + 1 + 10 + 2)
    result = weight_average(my_list)
    print("Average: {:0.2f}".format(result))