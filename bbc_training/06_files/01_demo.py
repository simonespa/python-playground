f = open("./test.txt", "w")

f.write("test")
print("Hello", file=f)
print("Bye", file=f)
