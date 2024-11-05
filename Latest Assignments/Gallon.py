ultimate_miles = 0
option = 0
count = 0
while option != -1:
    gallons_used = float(input("Enter the gallons used: "))
    miles_driven = float(input("Enter the miles driven: "))
    miles_per_gallon = miles_driven/gallons_used
    ultimate_miles += miles_per_gallon
    count += 1
    print("The miles/gallon for this tank was: ", miles_per_gallon)
    option = int(input("Do you want to quit (-1 for Yes and 0 for No): "))

    
else:
    overall_average_miles = ultimate_miles / count
    print("The overall average miles/gallon was:", overall_average_miles)
