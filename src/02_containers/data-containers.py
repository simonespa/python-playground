# List, Tuple, Set, Dictionaries

## List

print('# List')
list1 = list('Simone')
print(list1)
list2 = list([1, 2, 3])
print(list2)
list3 = [1, 2, 3]
print(list3)
list4 = [3, 'Simone', True, ['a', 'b']]
print(list4)
print(len(list4))

## Tuple

print()
print('# Tuple')

tuple1 = tuple(['Simone', 21, True])
print(tuple1)
tuple2 = ('Simone', 21, True)
print(tuple2)
tuple3 = 'Simone', 21, True
print(len(tuple3))

## Set

print()
print('# Set')

set1 = set([1, 1, 2, 2, 3, 3])
print(set1)
set2 = {1, 1, 2, 2, 3, 3}
print(set2)
set2.add(1)
print(set2)

## Dictionary

print()
print('# Dictionary')

# Dictionary with integer keys
my_dict = {1: 'A', 2: 'B'}
print(my_dict)

# Dictionary with string keys
my_dict = {'name': 'X', 'age': 10}
print(my_dict)

# Dictionary with mixed keys
my_dict = {'name': 'X', 1: ['A', 'B']}
print(my_dict)

# Example

groceries = []

for x in range(100):
  item = input('Enter item: ')
  if not item:
    break
  groceries.append(item)

for item in groceries:
  print(item)

list = list()
tuple = tuple()
set = set([1, 2, 2])
dictionary = dict(name='Simone')
print(dictionary)

## List Comprehensions

names = ['Simone', 'Jim', 'Tom', 'Marcos']
print([name for name in names if 'o' in name])
