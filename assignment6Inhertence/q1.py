class Account:
    def __init__(self,balance):
        self.balance = balance

    def check(self):
        print(f"{self.balance}")
    
    def deposit(self,amount):
        self.balance = self.balance + amount
        print(f"{self.balance}")

    def withdraw(self,amount):
        if amount > self.balance:
            print("insufficient balance")
        else:
            self.balance = self.balance - amount
            print(f"{amount}")

class S(Account):
    def calcul(self,rate):
        interest = self.balance * rate / 100
        print(f"{interest}")

acc = S(1000)
acc.check()
acc.deposit(343)
acc.withdraw(343)
acc.check()
acc.calcul(4)