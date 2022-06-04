list1 = list((1, 2, 3))
print(list1)
print(type(list1))

list2 = [1, 2, 3]
print(list2)
print(type(list2))

tuple1 = tuple(("Simone", 21, "London"))
print(tuple1)
print(type(tuple1))

tuple2 = ("Simone", 21, "London")
print(tuple2)
print(type(tuple2))

range = range(3)
print(range)
print(type(range))

dictionary1 = dict(name="Simone", surname="Spaccarotella")
print(dictionary1)
print(type(dictionary1))

dictionary2 = {"name": "Simone", "surname": "Spaccarotella"}
print(dictionary2)
print(type(dictionary2))

set1 = set(("apple", "banana", "banana", "cherry"))
print(set1)
print(type(set1))

set2 = {"apple", "banana", "banana", "cherry"}
print(set2)
print(type(set2))

# Example 1

groceries = []

for x in range(100):
    item = input("Enter item: ")
    if not item:
        break
    groceries.append(item)

for item in groceries:
    print(item)

list = list()
tuple = tuple()
set = set([1, 2, 2])
dictionary = dict(name="Simone")
print(dictionary)

# Example 2

inventory = {"bread": 5, "milk": 10, "egg": 1}

for product, price in inventory.items():
    print(f"The {product} cost {price}£")
