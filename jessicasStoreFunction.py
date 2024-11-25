products = {
    "Laptop": 1000,
    "Phone": 500,
    "Headphones": 100
}

cart = []

def add_to_cart(cart, products, product_name):
    if product_name in products:
        cart.append(product_name)
        return(f"{product_name} has been added to your cart.")
    else:
        return("Product not found.")

def view_cart(cart, products):
    if cart == 0:
        return("Your cart is currently empty.")
    else:
        for item in cart:
            return(f"{item} - ${products[item]}")

def remove_from_cart(cart, product_name):
    if product_name in cart:    
        cart.remove(product_name)
        return(f"{product_name} has been removed from your cart.")
    else:
        return("Item not found in cart.")

def calculate_total(cart, products):
    total = 0
    for item in cart:
        total += products[item]
    return total

def checkout(cart, products):
    total = calculate_total(cart, products)
    return(f"Thank you for shopping with us! Your total is ${total}.")
    cart.clear()

    while True:
        return("\nWelcome to Jessica's E-Store!")
        return("1. View Products")
        return("2. Add to Cart")
        return("3. Remove from Cart")
        return("4. View Cart")
        return("5. Checkout")
        return("6. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        for product, price in products.items():
            return(f"{product} - ${price}")
    elif choice == "2":
        product_name = input("Enter the product name to add to your cart: ")
        add_to_cart(cart, products, product_name)
    elif choice == "3":
        product_name = input("Enter the product name to remove from your cart: ")
        remove_from_cart(cart, product_name)
    elif choice == "4":
        view_cart(cart, products)
    elif choice == "5":
        checkout(cart, products)
    elif choice == "6":
        return("Thank you for visiting Jessica's E-Store. Goodbye!")

