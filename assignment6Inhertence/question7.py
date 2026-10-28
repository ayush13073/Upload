"""
Question 7: Method Overriding.
Base class: PaymentGateway with method process_payment(self, amount)
Derived class: CreditCardPayment(PaymentGateway) with method process_payment(self, amount)
Derived class: UPIPayment(PaymentGateway) with method process_payment(self, amount)
"""


class PaymentGateway:
    def process_payment(self, amount):
        print("Processing payment of", amount, "through generic gateway")


class CreditCardPayment(PaymentGateway):
    def process_payment(self, amount):
        print("Processing credit card payment of", amount)


class UPIPayment(PaymentGateway):
    def process_payment(self, amount):
        print("Processing UPI payment of", amount)


card = CreditCardPayment()
card.process_payment(500)

upi = UPIPayment()
upi.process_payment(300)
