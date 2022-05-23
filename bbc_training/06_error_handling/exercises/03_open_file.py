'''
filename = input("Enter a file to open? ")
f = open(filename)

This code can cause a number of different exception types. Try to find at least 3 different types of exceptions and write code to handle each type with its own error message.
'''

try:
  filename = input("Enter a file to open? ")
  f = open(filename)
except FileNotFoundError as e:
  print(f'Error: {e}')
