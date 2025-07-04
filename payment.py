from abc import ABC,abstractmethod

class PaymentMethod(ABC):
    @abstractmethod
    def process_payment(self,amount):
        pass

class CreditCardPayment(PaymentMethod):
    def process_payment(self,amount):
        print(f"Payment of ${amount} completed using Credit Card.")

class PayPalPayment(PaymentMethod):
    def process_payment(self, amount):
        print(f"Payment of ${amount} completed using PayPal.")