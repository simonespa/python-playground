try:
    f = open("file.json", "r")
    print(f.read())
except FileNotFoundError as e:
    print(f"Error: {e}")
finally:
    f.close()


# This construct is so common, that you can automatically close the file with the "with" syntax
# The following is equivalent

# it implements ContextManager class
with open("file.json", "r") as f:
    print(f.read())

# You can also wrap it in try block

try:
    with open("file.json", "r") as f:
        print(f.read())
except:
    print("error")
