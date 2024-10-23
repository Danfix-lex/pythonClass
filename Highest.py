largest = 0
validator = 11
for count in range(1, validator):
    if validator <= 11:
        score = int(input(f"Enter number" "{count}:"))
        if score > 0 and score <= 100:
            if score > largest:
                largest = score
        else:
            print("Invalid input!!!")
            validator -=1
print(f"The largest number is {largest}")
