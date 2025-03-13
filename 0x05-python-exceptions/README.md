# Python Exceptions Project

## SE Foundations - 0x05. Python - Exceptions

### Project Overview
This project is part of the **SE Foundations** series, focusing on **Python exceptions**. It provides hands-on experience with handling errors and exceptions in Python. Understanding exceptions is essential for writing robust and error-resistant Python programs.

### Learning Objectives
By the end of this project, you should be able to explain:
- Why Python programming is awesome
- The difference between **errors** and **exceptions**
- What exceptions are and how to use them effectively
- When and why exceptions should be used
- How to correctly handle exceptions
- The purpose of catching exceptions
- How to raise built-in exceptions
- When to implement clean-up actions after an exception

---

## Project Requirements
- **Programming Language**: Python (version 3.8.5)
- **Operating System**: Ubuntu 20.04 LTS
- **Code Formatting**: Must adhere to **pycodestyle** (version 2.8.*)
- **Execution**:
  - All files should be executable
  - Files should end with a new line
  - The first line of all scripts must be `#!/usr/bin/python3`
- **Editors**: You can use **vi, vim, or emacs**
- **Plagiarism Policy**: Strictly forbidden. You must write your own solutions.
- **README**: A `README.md` file at the root directory is mandatory.

---

## Tasks
### 0. Safe List Printing
- **File**: `0-safe_print_list.py`
- **Function**: `def safe_print_list(my_list=[], x=0):`
- **Objective**: Print `x` elements from a list.
- **Constraints**:
  - The list can contain any data type.
  - If `x` is greater than the list length, print as many as possible.
  - Use `try/except` to handle errors.
  - Do not use `len()`.

### 1. Safe Printing of an Integer
- **File**: `1-safe_print_integer.py`
- **Function**: `def safe_print_integer(value):`
- **Objective**: Print an integer using `{:d}.format()`.
- **Constraints**:
  - Returns `True` if `value` is an integer, otherwise `False`.
  - Use `try/except` to catch errors.
  - Do not use `type()`.

### 2. Print and Count Integers
- **File**: `2-safe_print_list_integers.py`
- **Function**: `def safe_print_list_integers(my_list=[], x=0):`
- **Objective**: Print the first `x` elements of a list, but only integers.
- **Constraints**:
  - Skips non-integer values silently.
  - If `x` is larger than the list length, an exception should be handled.
  - Do not use `len()`.

### 3. Integers Division with Debug
- **File**: `3-safe_print_division.py`
- **Function**: `def safe_print_division(a, b):`
- **Objective**: Divide two integers and print the result.
- **Constraints**:
  - Print result inside `finally` using `Inside result: ...`.
  - Return the division result or `None` if division fails.

### 4. Divide a List
- **File**: `4-list_division.py`
- **Function**: `def list_division(my_list_1, my_list_2, list_length):`
- **Objective**: Element-wise division of two lists.
- **Constraints**:
  - Returns a new list of length `list_length`.
  - If an error occurs (wrong type, division by zero, or out of range), print an appropriate message.
  - Use `try/except/finally`.

### 5. Raise Exception
- **File**: `5-raise_exception.py`
- **Function**: `def raise_exception():`
- **Objective**: Raise a **TypeError** exception.
- **Constraints**:
  - Use `raise` keyword.

### 6. Raise Exception with Message
- **File**: `6-raise_exception_msg.py`
- **Function**: `def raise_exception_msg(message=""):`
- **Objective**: Raise a **NameError** exception with a custom message.
- **Constraints**:
  - Use `raise` keyword with a message.

---

## Repository Information
- **GitHub Repository**: `alx-higher_level_programming`
- **Directory**: `0x05-python-exceptions`
- **Files**:
  - `0-safe_print_list.py`
  - `1-safe_print_integer.py`
  - `2-safe_print_list_integers.py`
  - `3-safe_print_division.py`
  - `4-list_division.py`
  - `5-raise_exception.py`
  - `6-raise_exception_msg.py`

---

## Author
This project was completed as part of the **ALX SE Program**.

### **Happy Coding! 🚀**

