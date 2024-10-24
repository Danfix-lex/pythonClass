numberOne = float(input("Enter your height(inches): "))
numberTwo = float(input("Enter your weight(pounds): "))

height = (numberOne * 0.0254)**2
weight = numberTwo*0.45359237

bmi = weight / height
rounded_bmi = round(bmi, 4)
print(rounded_bmi)


