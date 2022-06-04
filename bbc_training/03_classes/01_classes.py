class Person:
    def __init__(self, name, age) -> None:
        self.name = name
        self.age = age

    def get_name(self) -> str:
        return self.name

    def __str__(self) -> str:
        return f"{self.name} - {self.age}"


p = Person("Simone", 3)
print(p.get_name())
print(p.age)
print(p)
