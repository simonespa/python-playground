# Docs
# https://docs.python.org/3/library/stdtypes.html
# https://docs.python.org/3/library/string.html

# Boolean
# Booleans are a subtype of integers.
isTrue = True
isFalse = False
print(f"isTrue: {type(isTrue)} - {isTrue}")
print(f"isFalse: {type(isFalse)} - {isFalse}")

# Boolean operations
booleanAnd = isTrue and isFalse
booleanOr = isTrue or isFalse
booleanNot = not isTrue
print(f"booleanAnd: {type(booleanAnd)} - {booleanAnd}")
print(f"booleanOr: {type(booleanOr)} - {booleanOr}")
print(f"booleanNot: {type(booleanNot)} - {booleanNot}")

# Numeric Types — int, float, complex
# Integers have unlimited precision. Floating point numbers are usually implemented using double in C;
age = 21
miles = 1.6
integerNumber = int(3)
floatingNumber = float(5)
complexNumber = complex(3, 2)
print(f"age: {type(age)} - {age}")
print(f"miles: {type(miles)} - {miles}")
print(f"integerNumber: {type(integerNumber)} - {integerNumber}")
print(f"floatingNumber: {type(floatingNumber)} - {floatingNumber}")
print(f"complexNumber: {type(complexNumber)} - {complexNumber}")

# String
#
name = "Simone"
print(name)
print(type(name))
print(len(name))

# Concatenation
surname = "Spaccarotella"
print(name + " " + surname)

# Other string operations
print(name.upper())
print(name[1:3])
print(name[1])

# age = input('Enger your age: ');
# print('You were born in ' + (2022 - age))
# TypeError: unsupported operand type(s) for -: 'int' and 'str'

# age = int(input('Enger your age: '));
# print('You were born in ' + (2022 - age))
# TypeError: can only concatenate str (not "int") to str

age = int(input("Enger your age: "))

print("You were born in " + str(2022 - age))

# the space is added automatically
print("You were born in", 2022 - age)

print(f"You were born in {2022 - age}")

# The "f" strings

name = input("Enter your name: ")
message = f"Hello {name}"
print(message)
