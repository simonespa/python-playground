# https://codesensei.nl/courses/shared/exercises/dictionaries.html

# Warming up

# myself = {'name': 'Simone', 'age': 38, 'city': 'London'}
# myself['phone'] = '00000000'
# myself['city'] = 'Rome'

# print(myself)

# Ip adresses

# lookup = {}
# while True:
#   server = input('Server name: ')
#   ip = input('IP: ')
#   lookup[server] = ip
#   print(lookup)
#   keepRunning = input('Continue (y/n): ')
#   if (keepRunning.upper() == 'N'):
#     break

# Grades

grades = {'John': [8, 2, 3, 6, 8],
 'Annie': [5, 8, 7, 8, 5],
 'Pete': [8, 8, 6, 7, 9],
 'Lucy': [2, 4, 5, 6, 7],
 'Bob': [6, 7, 5, 6, 7]}

# name = input('Give me a name: ')

# nameGrades = grades[name]
# sum = 0
# for x in range(len(nameGrades)):
#   sum += nameGrades[x]

# print(f'The averate for {name} is {sum / len(nameGrades)}')

# Class overview

keys = grades.keys()

for person in grades:
  ithGrades = grades[person]
  sum = 0
  for grade in ithGrades:
    sum += grade
  print(f'The average for {person} is {sum / len(ithGrades)}')
