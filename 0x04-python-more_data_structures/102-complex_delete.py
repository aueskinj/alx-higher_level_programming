#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    matching_keys = [key for key, Value in a_dictionary.items() if Value == value]
    print(matching_keys)
    return ({k: v for k, v in a_dictionary.items() if k not in matching_keys})

if __name__ == "__main__":
    complex_delete = __import__('102-complex_delete').complex_delete
    print_sorted_dictionary = \
        __import__('6-print_sorted_dictionary').print_sorted_dictionary

    a_dictionary = {'lang': "C", 'track': "Low", 'pref': "C", 'ids': [1, 2, 3]}
    new_dict = complex_delete(a_dictionary, 'C')
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)

    print("--")
    print("--")
    new_dict = complex_delete(a_dictionary, 'c_is_fun')
    print_sorted_dictionary(a_dictionary)
    print("--")
    print_sorted_dictionary(new_dict)