"""
Question 1: Create basic bank application with functionality deposit(), withdraw() and check_balance().
Base Class is Account with methods check_balance(), deposit(), withdraw().
Derived class is SavingAccount with method calculate_interest().
(Hint: Single Inheritance)
"""


class Account:
    def __init__(self, balance):
        self.balance = balance

    def check_balance(self):
        print("Balance:", self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited", amount, "New balance:", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough balance")
        else:
            self.balance = self.balance - amount
            print("Withdrawn", amount, "New balance:", self.balance)


class SavingAccount(Account):
    def calculate_interest(self, rate):
        interest = self.balance * rate / 100
        print("Interest at", rate, "% =", interest)


account = SavingAccount(1000)
account.check_balance()
account.deposit(500)
account.withdraw(200)
account.calculate_interest(5)
