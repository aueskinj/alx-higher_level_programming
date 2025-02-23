#!/usr/bin/python3

def fizzbuzz():
    '''showing multiples of three(fizz) and five(buzz)'''
    for i in range(1, 101):
        if i % 5  == 0 and i % 3 == 0:
            print('FizzBuzz ', end="")
            continue
        elif i % 3 == 0:
            print('Fizz ', end='')
        elif i % 5 == 0:
            print('Buzz ', end='')

        else:
            print('{} '.format(i), end='')
