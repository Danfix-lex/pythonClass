userNumbers = [1, 2, 3, 6, 8, 10, 1]
evenNumbers = 0
oddNumbers = 0
oddAndEvenNumbers = []
for number in userNumbers:
    if number % 2 == 1:
        oddNumbers += 1
    else:
        evenNumbers += 1
oddAndEvenNumbers.append(oddNumbers)
oddAndEvenNumbers.append(evenNumbers)
print(oddAndEvenNumbers)
