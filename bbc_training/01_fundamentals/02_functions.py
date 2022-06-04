# Function
def greet(name):
    print(f"Hi {name}")


# Default values with Python docstrings
def add(a=0, b=0):
    """This function adds two numbers"""
    return a + b


print(add(1, 2))
print(add(a=1, b=1))
print(add(b=1, a=1))
print(add())
print(add(1))


# Named variables
def message(name, message):
    print(f"{name} has a message: {message}")


message("Simone", "hi there")
message(name="Simone", message="hello")
message(message="hello", name="Simone")


# Returning a tuple
def swap(a, b):
    return b, a


print(swap(1, 2))
x, y = swap(1, 2)
print(x, y)


# Arbitrary parameters
def addMore(*args):
    return sum(args)


print(addMore())
print(addMore(2))
print(addMore(2, 3))
