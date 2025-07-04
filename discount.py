from abc import ABC,abstractmethod

class Discount(ABC):
    @abstractmethod
    def apply_discount(self,total):
        pass

class FlatDiscount(Discount):
    def __init__(self,discount_amount):
        self.discount_amount=discount_amount
    def apply_discount(self, total):
        return max(0,total - self.discount_amount)
    
class PercentageDiscount(Discount):
    def __init__(self, percentage):
        self.percentage = percentage
    def apply_discount(self, total):
        return total * (1-self.percentage/100)

    