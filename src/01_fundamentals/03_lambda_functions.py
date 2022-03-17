# Lambdas

persons = [
  ('Z', 24),
  ('A', 31),
  ('D', 21)
]

def get_name(person):
  return person[0]

def get_age(person):
  return person[1]

persons.sort(key=get_name)
print(persons)

persons.sort(key=get_age)
print(persons)

persons.sort(key=lambda person: person[0])
print(persons)
