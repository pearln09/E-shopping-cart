from datetime import datetime

class Order:
    def __init__(self,customer,cart,total_amount,payment_method):
        self.customer = customer
        self.items=cart.items.copy()
        self.total_amount=total_amount
        self.payment_method=payment_method
        self.date=datetime.now()

    def order_summary(self):
        print(f"\nOrder Summary for {self.customer.name}")
        for product,qty in self.items.items():
            print(f"{product.name} - {qty} items")
        print(f"Total Paid: ${self.total_amount}")
        print(f"Payment Method: {self.payment_method.__class__.__name__}")
        print(f"Order date: {self.date.strftime('%Y-%m-%d %H:%M:%S')}")
        
