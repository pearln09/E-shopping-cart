from product import Product,load_products_from_txt
from customer import Customer
from payment import CreditCardPayment, PayPalPayment
from discount import FlatDiscount,PercentageDiscount
from order import Order

products = load_products_from_txt(r'C:\Users\Pearl Narang\Desktop\My Practice\E-shopping\products.txt')

print("\nWelcome to the E-shop!")
cust_id=int(input("Enter your Customer ID:"))
cust_name=input("Enter your Name:")
cust_email=input("Enter your Email:")

customer=Customer(cust_id,cust_name,cust_email)

def display_products():
    print("\nAvailable products: ")
    for product in products:
        product.display_info()

def add_to_cart():
    display_products()
    try:
        product_id=int(input("\nEnter the Product ID to add to cart:"))
        quantity=int(input("Enter the quantity:"))
        product=next((p for p in products if p.product_id==product_id),None)
        if product:
            customer.cart.add_product(product,quantity)
            print(f"\nProduct {product.name} added to your cart successfully!")
        else:
            print("Product not found!")
    except ValueError:
        print("Invalid input!")

def view_cart():
    customer.cart.view_items()

def checkout():
    if customer.cart.items==None:
        print("/nYour cart is empty")
        return
    total = customer.cart.calculate_total()
    print(f"\nYour total bill is: ${total}")

    print("\nApply Discount: ")
    print("1. Flat Discount ($500 off)")
    print("2. Percentage Discount (10% off)")
    print("3. No Discount")
    discount_choice = input("Enter choice: ")

    if discount_choice=='1':
        discount = FlatDiscount(500)
    elif discount_choice=='2':
        discount = PercentageDiscount(10)
    else:
        discount=None
    
    if discount:
        total=discount.apply_discount(total)
        print(f"Total after discount: ${total}")
    
    print("\nChoose payment method: ")
    print("1. Credit Card")
    print("2. PayPal")
    payment_choice=input("Enter choice: ")

    if payment_choice=='1':
        payment=CreditCardPayment()
    elif payment_choice=='2':
        payment=PayPalPayment()
    else:
        print("Invalid payment method")

    payment.process_payment(total)

    order=Order(customer,customer.cart.items,total,payment.__class__.__name__)
    order.save_order(r'C:\Users\Pearl Narang\Desktop\My Practice\E-shopping\orders.txt')
    print("\nOrder placed successfully! Order saved.")

    customer.cart.items.clear()

while True:
    print("n--- E-commerce Menu ---")
    print("1. View Products")
    print("2. Add to Cart")
    print("3. View Cart")
    print("4. Checkout")
    print("5. Exit")

    choice= input("Enter your choice: ")

    if choice=='1':
        display_products()
    elif choice=='2':
        add_to_cart()
    elif choice=='3':
        view_cart()
    elif choice=='4':
        checkout()
    elif choice=='5':
        print("Thank you for shopping with us!")
        break
    else:
        print("Invalid choice. Please choose from the above choices.")
    


