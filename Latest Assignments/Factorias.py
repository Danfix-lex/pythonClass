numbers = int(input("Enter number: "))
factoria = 1
for count in range(1, (numbers + 1)):
    factoria *= (numbers + 1) - count
print(factoria)
