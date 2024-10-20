amount_of_investment = int(input("Enter amount to invest: "))
annual_rate_of_return = (7/100)*1000
print(annual_rate_of_return)
number_of_years = int(input("Enter number of years to invest: "))
investment_return = amount_of_investment*(1+annual_rate_of_return)**number_of_years
print(investment_return)
