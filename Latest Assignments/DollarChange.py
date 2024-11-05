money = int(input("Enter your purchase price for the item (Dollar): "))
quarters = money // 25
remainder = money % 25
dimes = remainder // 10
pennies = remainder % 10
print("Your change is: ")
print(quarters, "quarters")
print(dimes, "dimes")
print(pennies, "pennies")
