import math
principal = float(input("Enter the principal amount: "))

interest_rate = float(input("Enter the annual interest rate: "))
rate = interest_rate / 100

choice = float(input("Do you want to calculate for (1): Day(s) or (2): Week(s) or (3): Year(s)? Enter 1 or 2 or 3: "))

time_in_years = 0
compounded = 0

if choice == 1:
    days = float(input("Enter the number of day(s): "))
    time_in_years = days / 365.0
    compounded = 365
elif choice == 2:
    weeks = float(input("Enter the number of Week(s): "))
    time_in_years = weeks / 52.0
    compounded = 52.0
elif choice == 3:
    years = float(input("Enter the number of year(s): "))
    time_in_years = years / 1.0
    compounded = 1
else:
    print("Invalid choice! Please try again.")

amount = principal * math.pow(1 + (rate / compounded), compounded * time_in_years)
compound_interest = amount - principal

print(amount)
print(compound_interest)
