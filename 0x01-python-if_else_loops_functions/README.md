# Python - If/Else, Loops, and Functions

## Overview
This project is part of the **SE Foundations** track, focusing on Python programming, specifically control flow, loops, and functions. It provides practical exercises to strengthen your understanding of fundamental Python concepts.

## Learning Objectives
By the end of this project, you should be able to:

- Understand why Python programming is powerful and useful.
- Recognize the importance of indentation in Python.
- Use `if`, `if...else`, and `if...elif...else` statements.
- Implement comments effectively in Python code.
- Assign values to variables correctly.
- Use `while` and `for` loops and understand the difference between Python's `for` loop and C's `for` loop.
- Utilize `break` and `continue` statements.
- Apply `else` clauses in loops.
- Understand the `pass` statement and when to use it.
- Use the `range()` function effectively.
- Define and call functions in Python.
- Understand the behavior of functions without return statements.
- Recognize variable scope in Python.
- Interpret Python error messages and tracebacks.
- Use arithmetic operators effectively in Python.

## Resources
To complete this project, refer to the following resources:

- [More Control Flow Tools](https://docs.python.org/3/tutorial/controlflow.html) (Read until "4.6. Defining Functions" included)
- [IndentationError](https://www.python.org/dev/peps/pep-0008/#indentation)
- [How To Use String Formatters in Python 3](https://realpython.com/python-string-formatting/)
- [Learn to Program](https://greenteapress.com/thinkpython/html/thinkpython004.html)
- [Learn to Program 2: Looping](https://greenteapress.com/thinkpython/html/thinkpython005.html)
- [Pycodestyle – Style Guide for Python Code](https://pycodestyle.readthedocs.io/en/latest/)
- `man python3`

## Requirements
### Python Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- Files must be interpreted/compiled on **Ubuntu 20.04 LTS** using `python3 (version 3.8.5)`
- All files should end with a new line
- First line of all files must be exactly `#!/usr/bin/python3`
- Follow the `pycodestyle` (version 2.8.*) style guide
- All files must be executable
- File length will be tested using `wc`

### C Scripts
- Allowed editors: `vi`, `vim`, `emacs`
- Compilation will be done on **Ubuntu 20.04 LTS** using `gcc` with the flags: `-Wall -Werror -Wextra -pedantic -std=gnu89`
- Files must end with a new line
- Follow the **Betty style** (checked using `betty-style.pl` and `betty-doc.pl`)
- No use of global variables
- Maximum of **5 functions per file**
- Function prototypes should be in a header file named `lists.h`
- Header files should have include guards

## Tasks
### 0. Positive anything is better than negative nothing
Write a program that assigns a random signed number to the variable `number` and prints whether it is positive, zero, or negative.

**File:** `0-positive_or_negative.py`

### 1. The last digit
Modify the given program to print the last digit of `number` along with its classification.

**File:** `1-last_digit.py`

### 2. I sometimes suffer from insomnia...
Write a program that prints the lowercase ASCII alphabet without using stored variables or importing modules.

**File:** `2-print_alphabet.py`

### 3. When I was having that alphabet soup...
Print the lowercase ASCII alphabet, excluding 'q' and 'e'.

**File:** `3-print_alphabt.py`

### 4. Hexadecimal printing
Write a program that prints numbers from 0 to 98 in both decimal and hexadecimal format.

**File:** `4-print_hexa.py`

### 5. 00...99
Print numbers from 0 to 99, formatted as `00, 01, 02, ..., 99`.

**File:** `5-print_comb2.py`

### 6. Inventing is a combination of brains and materials...
Print all possible different combinations of two digits in ascending order.

**File:** `6-print_comb3.py`

### 7. Is lower?
Write a function that checks for lowercase characters.

**File:** `7-islower.py`

### 8. To uppercase
Write a function that prints a string in uppercase.

**File:** `8-uppercase.py`

### 9. There are only 3 colors, 10 digits...
Write a function that prints the last digit of a number.

**File:** `9-print_last_digit.py`

### 10. a + b
Write a function that adds two integers and returns the result.

**File:** `10-add.py`

### 11. a ^ b
Write a function that computes `a` raised to the power of `b`.

**File:** `11-pow.py`

### 12. Fizz Buzz
Write a function that prints numbers from 1 to 100 with FizzBuzz rules.

**File:** `12-fizzbuzz.py`

### 13. Insert in sorted linked list (Advanced)
Write a function in C to insert a number into a sorted singly linked list.

**File:** `13-insert_number.c`

## Repository Structure
```
├── 0x01-python-if_else_loops_functions
│   ├── 

│   ├── 1-last_digit.py
│   ├── 2-print_alphabet.py
│   ├── 3-print_alphabt.py
│   ├── 4-print_hexa.py
│   ├── 5-print_comb2.py
│   ├── 6-print_comb3.py
│   ├── 7-islower.py
│   ├── 8-uppercase.py
│   ├── 9-print_last_digit.py
│   ├── 10-add.py
│   ├── 11-pow.py
│   ├── 12-fizzbuzz.py
│   ├── 13-insert_number.c
│   ├── lists.h
│   ├── README.md
```

## How to Run the Scripts
Ensure you have `Python 3.8.5` installed on **Ubuntu 20.04 LTS**.

To run a script:
```bash
chmod +x script_name.py
./script_name.py
```

For C programs, compile and run as follows:
```bash
gcc -Wall -Werror -Wextra -pedantic -std=gnu89 file.c -o output
./output
```

## Author
This project was developed as part of **ALX Higher Level Programming** coursework.

---
By completing these tasks, you will have gained a solid foundation in Python control flow, loops, and functions. Happy coding!

