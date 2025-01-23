userNumbers = [5, 3, 7, 9, 2, 8]
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
