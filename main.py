from product import Product
from customer import Customer
from payment import CreditCardPayment, PayPalPayment
from discount import FlatDiscount,PercentageDiscount
from order import Order

p1=Product(101,"Laptop",60000,10,"Electronics")
p2 = Product(102, "Book: Python 101", 500, 20, "Books")
p3 = Product(103, "Headphones", 1500, 15, "Electronics")

customer = Customer(1,"Pearl","reachpearlnarang@gmail.com")

p1.display_info()
p2.display_info()
p3.display_info()

customer.cart.add_product(p1,1)
customer.view_cart()

discount = PercentageDiscount(10)
total = customer.cart.calculate_total()
total_after_discount=discount.apply_discount(total)
print(f"Total after discount: ${total_after_discount}")

payment_method=CreditCardPayment()
payment_method.process_payment(total_after_discount)

order=Order(customer,customer.cart,total_after_discount,payment_method)
order.order_summary()

customer.cart.items.clear()