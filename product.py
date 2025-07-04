class Product:
    def __init__(self,product_id,name,price,stock,category,description=""):
        self.product_id=product_id
        self.name=name
        self.price=price
        self.stock=stock
        self.category=category
        self.description=description
    def update_stock(self,quantity):
        if quantity<=self.stock:
            self.stock=self.stock-quantity
        else:
            raise ValueError(f"Only {self.stock} items available in stock.")
    def is_available(self,quantity):
        return self.stock>=quantity
    def display_info(self):
        print(f"[{self.product_id}]{self.name}({self.category}) - ${self.price} ; Stock: {self.stock}")