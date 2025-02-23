#!/usr/bin/python3
import random

number = random.randint(-10000, 10000)  # Generate a random number

# Extract last digit while preserving sign
last_digit = abs(number) % 10  # Get the last digit as a positive integer

# Retain the original sign if the number is negative
if number < 0:
    last_digit = -last_digit

if last_digit > 5:
    print(f"Last digit of {number} is {last_digit} and is greater than 5")
elif last_digit < 6 and last_digit != 0:
    print(f"Last digit of {number} is {last_digit} 
          and is less than 6 and not 0")
elif last_digit == 0:
    print(f"Last digit of {number} is {last_digit} and is 0")
