class Person:
  def __init__(self, name, age) -> None:
    self.name = name
    self.age = age

  def get_name(self):
    return self.name

p = Person('Simone', 3)
print(p.get_name())
print(p.age)
