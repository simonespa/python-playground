# https://codesensei.nl/courses/shared/exercises/for.html

# Range

# for n in range(101):
#   print(n ** 2)

# Greetings

# name = input('What is your name? ')
# len = len(name)

# for i in range(1, len + 1):
#   print(f'{i}) Hi {name}')

# A list of words

# words = []
# for x in range(4):
#   word = input('Enter a random word: ')
#   words.append(word)

# words.sort()
# print(words)
# words.reverse()
# print(words)

# for x in range(len(words)):
#   words[x] = words[x].upper()

# print(words)

# for x in range(len(words)):
#   print(words[x][0])

# Names and Ages

list = [
    ["John", "Smith", 32],
    ["Peter", "Jones", 50],
    ["Anna", "Karenina", 44],
    ["Guido", "Van Rossum", 54],
]

# for x in range(len(list)):
#   print(list[x][1])

# sum = 0
# for x in range(len(list)):
#   sum += list[x][2]

# print(f'The average age is {sum / len(list)}')

# Sorting

# surnames = []
# for x in range(len(list)):
#   surnames.append(list[x][1])

# surnames.sort()
# print(surnames)

# Tuition

# increase = 6 # every year

# tuition = 10000

# for x in range(2):
#   tuition += tuition * 6 / 100

# print(tuition)

# Pyramid
