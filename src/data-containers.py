# # List

# list1 = [1, 2, 3]
# list2 = [3, 5.6, 'Simone', [1, 2, 'Spaccarotella']]
# len(list2)
# list2.append(True)
# list3 = list()

# tuple1 = ('Simone', 21, True)
# tuple2 = 'Simone', 21, True

# dictionary1 = {'Name': 'Simone', 'Surname': 'Spaccarotella'}
# dictionary2 = {'Simone': '0309890333', 'Laura': '939039383'}

# set = {2, 3, 4, 5}
# print(set)
# set.add(2)
# print(set)

# groceries = []

# for x in range(100):
#   item = input('Enter item: ')
#   if not item:
#     break
#   groceries.append(item)

# for item in groceries:
#   print(item)

# list = list()
# tuple = tuple()
# set = set([1, 2, 2])
# dictionary = dict(name='Simone')
# print(dictionary)

## List Comprehensions

names = ['Simone', 'Jim', 'Tom', 'Marcos']
print([name for name in names if 'o' in name])
