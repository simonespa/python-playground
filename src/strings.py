# Docs: https://docs.python.org/3/library/string.html

# Length of the string
name = 'Simone'
print(len(name))

# Concatenation
surname = 'Spaccarotella'
print(name + ' ' + surname)

#
print(name.upper())
print(name[1:3])
print(name[1])

# age = input('Enger your age: ');
# print('You were born in ' + (2022 - age))
# TypeError: unsupported operand type(s) for -: 'int' and 'str'

# age = int(input('Enger your age: '));
# print('You were born in ' + (2022 - age))
# TypeError: can only concatenate str (not "int") to str

age = int(input('Enger your age: '));
print('You were born in ' + str(2022 - age))

# the space is added automatically
print('You were born in', 2022 - age)

print(f'You were born in {2022 - age}')

# The "f" strings

name = input('Enter your name: ')
message = f"Hello {name}"
print(message)
