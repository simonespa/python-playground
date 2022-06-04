# Bank Account: https://codesensei.nl/courses/shared/exercises/classes_2.html


class BankAccount:
    def __init__(self, name, initial_balance):
        self.name = name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            return self.balance
        else:
            print("Can't deposit a negative amount!")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.balance:
                self.balance -= amount
                return self.balance
            else:
                print("Insufficient balance!")
        else:
            print("Can't withdraw nonpositive amount!")

    def __str__(self) -> str:
        return "dfd"

    def __repr__(self) -> str:
        return "dfd"


a = BankAccount("Simone", 10000)
print(a)
