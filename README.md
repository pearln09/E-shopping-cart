# E-Commerce Shopping Cart Simulator in Python
An end-to-end Object-Oriented Programming (OOP) based command-line e-commerce simulator, built with Python.
This project demonstrates encapsulation, inheritance, polymorphism, and file handling, creating a complete e-commerce simulation.

**A. Features:**
- View available products
- Add products to a shopping cart
- Apply discounts (Flat / Percentage)
- Process payments (Credit Card / PayPal)
- Load products from a .txt file
- Save orders to an order log file
- Exception handling for stock availability and invalid inputs

**B. OOP Concepts Used:**
Concepts:
- *Encapsulation*: Private product, order, and customer data in classes
- *Inheritance*: CreditCardPayment, PayPalPayment inherit from Payment
- *Polymorphism*: apply_discount() and process_payment() method overriding
- *Abstraction*: Simplified CLI hiding internal class structure

**C. Project Structure:**

```bash
E-shopping/
├── main.py               # Main CLI program
├── product.py             # Product class + file loader
├── customer.py            # Customer & Cart classes
├── payment.py             # Payment classes
├── discount.py            # Discount strategy classes
├── order.py               # Order generation & saving
├── products.txt           # Product database
└── orders.txt             # Auto-generated order summaries
```

**D. Example Products (products.txt)**

```bash
101,Laptop,60000,10,Electronics,High-end gaming laptop
102,Python Book,500,50,Books,Programming basics
103,Headphones,1500,20,Electronics,Noise cancelling
104,Smartphone,45000,8,Electronics,Latest model with 5G support
```

**E. ▶️ Getting Started**

*1. Clone the Repo:*
```bash
git clone https://github.com/your-username/e-shopping-simulator.git
cd e-shopping-simulator
```

*2. Run the Application:*
```bash
python main.py
```

**F. Example CLI Usage:**

```bash
--- E-Commerce CLI Menu ---
1. View Products
2. Add to Cart
3. View Cart
4. Checkout
5. Exit

Enter your choice: 1
```

**G. Order History Example (orders.txt)**

```bash
Customer: Pearl, Total: ₹54000.0, Payment: PayPal
Laptop x 1
Headphones x 2
```

**H. Built With:**

1. Python 3.x
2. Object-Oriented Programming (OOP)
3. File I/O
4. Simple CLI Interface

