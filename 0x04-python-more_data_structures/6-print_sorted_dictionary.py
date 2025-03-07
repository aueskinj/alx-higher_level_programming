#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    keys = list(a_dictionary)
    for i in sorted(keys):
        print("{}: {}".format(i, a_dictionary[i]) )

if __name__ == "__main__":
    print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary
    a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
    print_sorted_dictionary(a_dictionary)
