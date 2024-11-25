print("Welcome to Jessica's Store, we are glad that you are patronizing us!!!")

products = {
    "Laptop": 1000,
    "Phone": 500,
    "Headphones": 100
}

cart = []

while True:
    print("\nWelcome to Jessica's E-Store!")
    print("1. View Products")
    print("2. Add to Cart")
    print("3. Remove from Cart")
    print("4. View Cart")
    print("5. Checkout")
    print("6. Exit")
    
    choice = input("Enter your choice: ")

    if choice == "1":
        for product, price in products.items():
            print(f"{product} - ${price}")
    elif choice == "2":
        product_name = input("Enter the product name to add to your cart: ")
        if product_name in products:
            cart.append(product_name)
            print(f"{product_name} has been added to your cart.")
        else:
            print("Product not found.")
    elif choice == "3":
        product_name = input("Enter the product name to remove from your cart: ")
        if product_name in cart:
            cart.remove(product_name)
            print(f"{product_name} has been removed from your cart.")
        else:
            print("Item not found in cart.")
    elif choice == "4":
        if not cart:
            print("Your cart is currently empty.")
        else:
            for item in cart:
                print(f"{item} - ${products[item]}")
    elif choice == "5":
        total = 0
        for item in cart:
            total += products[item]
        print(f"Thank you for shopping with us! Your total is ${total}.")
        cart.clear()
    elif choice == "6":
        print("Thank you for visiting Jessica's E-Store. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")

