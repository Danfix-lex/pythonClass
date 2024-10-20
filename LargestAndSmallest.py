largest = float('-inf')
smallest = float('inf')
while True:
    num = float(input("Enter a number (or type 'done' to finish): "))
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num
    again = input("Do you want to enter another number? (yes/no): ")
    if again.lower() != "yes":
        break
print("Largest number:", largest)
print("Smallest number:", smallest)
