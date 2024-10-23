positive = 0
negative = 0
zero = 0

for i in range(5):
    number = int(input(f"Enter number {i + 1}: "))
    
    if number > 0:
        positive += 1
    elif number < 0:
        negative += 1
    else:
        zero += 1

print("Positive is:",positive, "Negative is:",negative, "Zero is:",zero)

