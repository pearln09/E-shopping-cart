class Cart:
    def __init__(self,customer):
        self.customer=customer
        self.items={}
    def add_product(self,product,quantity):
        if product.is_available(quantity):
            self.items[product]=self.items.get(product,0)+quantity
            product.update_stock(quantity)
            print(f"Added{quantity} x {product.name} to the cart.")
        else:
            raise Exception(f"{product.name} does not have enough stock.")
    def remove_product(self,product):
        if product in self.items:
            del self.items[product]
            print(f"Removed {product.name} from the cart")
    def view_items(self):
        if self.items==None:
            print("Your cart is empty")
            return
        print("Your Cart:")
        for product,quantity in self.items.items():
            print(f" - {product.name}: {quantity} items; ${product.price*quantity}")
        print(f"Total: ${self.calculate_total()}")
    def calculate_total(self):
        return sum(product.price*quantity for product,quantity in self.items.items())