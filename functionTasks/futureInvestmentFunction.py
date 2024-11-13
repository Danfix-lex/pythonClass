def get_future_investment(input1, input2, input3):
   if type (input1 and input2 and input3) in [int, float]:
        number_of_months = input3 * 12
        future_investment_amount = input1 * (1 + input2) ** number_of_months
        return round((future_investment_amount), 2)
        raise TypeError
