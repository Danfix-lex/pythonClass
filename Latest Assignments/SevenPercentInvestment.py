amount_of_investment = int(input("Enter amount to invest: "))
annual_rate_of_return = (7/100)
print(annual_rate_of_return)
for number_of_years in range(1, 31):
    investment_return = amount_of_investment*(1+annual_rate_of_return)**number_of_years
    print(f"{investment_return:.2f}")
