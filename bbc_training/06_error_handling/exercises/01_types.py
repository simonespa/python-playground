# https://codesensei.nl/courses/shared/exercises/exceptions.html

"""
For each of the following exception types, write a piece of code to cause that exception.

IndexError
NameError
TypeError
"""

from typing import Type


try:
    list = list()
    index = int(input("Enter an index: "))
    print(list[index])
except IndexError as e:
    print(f"Error: {e}")

try:
    print(unknownVariable)
except NameError as e:
    print(f"Error: {e}")

try:
    string = "name"
    integer = 3
    result = string / integer
except TypeError as e:
    print(f"Error: {e}")
