#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    # a_dictionary = {key: a_dictionary[key] for key in sorted(a_dictionary)}
    for key, value in sorted(a_dictionary), a_dictionary.values:
        print("{}:{}".format(key, value))

if __name__ == "__main__":
    print_sorted_dictionary = __import__('6-print_sorted_dictionary').print_sorted_dictionary
    a_dictionary = { 'language': "C", 'Number': 89, 'track': "Low level", 'ids': [1, 2, 3] }
    print_sorted_dictionary(a_dictionary)
