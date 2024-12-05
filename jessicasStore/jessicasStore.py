products = {

    "Laptop": 300000,
    "Phone": 250000,
    "Headphones": 10000,
    "Rice": 5000,
    "Beans": 8000,
    "Garri": 4000,
    "Fufu": 2000,
    "Pepper": 10000,
    "TV": 100000,
    "Generator": 250000
    
}

cart = []

while True:
    print("\nWelcome to Danfix's E-Store!")
    print("1. View Products")
    print("2. Add to Cart")
    print("3. Remove from Cart")
    print("4. View Cart")
    print("5. Checkout")
    print("6. Exit")

    choice = input("\nEnter your choice between (1-6): ")

    if choice == "1":
        print("\nThese are the list of Products available in our store that you can buy, more will be added and updated as time goes on:\n")
        for product, price in products.items():
            print(f"{product}: ₦{price}")

    elif choice == "2":
        product_name = input("\nEnter the product name to add to your cart as part of the item you want to buy from out store: ")
        if product_name in products:
            cart.append(product_name)
            print(f"\n{product_name} has been added to your cart.")
        else:
            print("\nProduct not found, please check the name of the item or probably you chose an item that is not on the display list to be bought.")

    elif choice == "3":
        product_name = input("\nEnter the product name to remove from your cart, that has just been added to the list of item(s) you want to buy from our store: \n")
        if product_name in cart:
            cart.remove(product_name)
            print(f"\n{product_name} has been removed from your cart.")
        else:
            print("\nProduct not found, please check the name of the item or probably you chose an item that is not on the list display to be bought.")

    elif choice == "4":
        if not cart:
            print("\nYour cart is currently empty, this is because you haven't bought anything yet.")
        else:
            print("\nYour cart:")
            for item in cart:
                print(f"\n{item}: ₦{products[item]}")

    elif choice == "5":
        total = sum(products[item] for item in cart)
        print(f"\nThank you for shopping with us! Your total payment is: ₦{total}.")
        cart.clear()

    elif choice == "6":
        print("\nThank you for visiting Danfix's E-Store and don't forget to patronise us next time. Goodbye!")
        break

    else:
        print("\nInvalid choice. Please try again.")

