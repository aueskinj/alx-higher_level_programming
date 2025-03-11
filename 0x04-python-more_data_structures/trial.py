#!/usr/bin/python3
# roman_string = 'IX'
# total = 0
# previous = 0


# for numeral in roman_string.upper():
#     print(rome[numeral])
#     current = rome[numeral]
#     if current > previous:
#         total = current - previous
#     else:
#         total += current
#     previous = current    # if rome[numeral] < rome[numeral + 1]:
#     #     rome[numeral] 
#     # pass
# print(total)

# def roman_to_int(roman_string):
#     if not isinstance(roman_string, str):
#         return None
#     rome = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
#     previous = 0
#     for numeral in roman_string.upper():
#         current = rome[numeral]
#         if current > previous:
#             total = current -previous
#         else: 
#             total =+ current
#         previous = current
#     print(total)
#     return total

# if __name__ == '__main__':
#     roman_string = 'LXXXVII'
#     roman_to_int(roman_string)

rome = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
roman_string = 'cl'
previous = 0


for numeral in roman_string.upper():
    print(rome[numeral])
    current = rome[numeral]
    if current > previous:
        total = current - previous
    else:
        total += current
    previous = current    # if rome[numeral] < rome[numeral + 1]:
    #     rome[numeral] 
    # pass
print(total)