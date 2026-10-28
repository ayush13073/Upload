class Payment:
    def processa(self,amount):
        print(f"amount processed %d {self.amount} ")

class credit(Payment):
    def processa(self, amount):
        self.amount = amount
        print(f"amount processed {self.amount} ")

class upi(Payment):
    def processa(self, amount):
        self.amount = amount
        print(f"amount processed {self.amount} ")

c = credit()
u = upi()

c.processa(343)
u.processa(5343)