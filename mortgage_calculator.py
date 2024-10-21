principal = int(input("Enter the amount you wish to borrow: "))
annual_interest_rate = int(input("Enter the amount of percentage: "))
monthly_interest = (annual_interest_rate/100)/12
duration = int(input("Enter the number of duration you wish the loan to extend(in years): "))
monthly_duration = duration*12
monthly_payment = principal*monthly_interest*(1+monthly_interest)**duration/((1+monthly_interest)**duration-1)
print(f"\nYour monthly payment is: {monthly_payment:.2f}")
