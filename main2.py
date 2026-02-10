class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

class Bank:
    def add_money(self, acc, money):
        acc.balance += money

    def take_money(self, acc, money):
        acc.balance -= money


a = BankAccount("Іра", 500)
b = Bank()

b.add_money(a, 200)
print(a.balance)
