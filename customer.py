from cart import Cart

class Customer:
    def __init__(self,customer_id,name,email):
        self.customer_id = customer_id
        self.name = name
        self.email=email
        self.cart=Cart(self)
    
    def view_cart(self):
        self.cart.view_items()