validator = 1
largest = -1

while validator <= 10:
    count = validator
    score = int(input(f"Enter number {count}: "))
    if score > 0 and score <= 100:
        if score > largest:
            largest = score
        validator += 1
    else:
        print("Invalid input")
        
print("Largest is:", largest)
