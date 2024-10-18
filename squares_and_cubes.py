numbers = []
for i in range(5):
    number = int(input("Enter just a number: "))
    numbers.append(number) 


print("number\tsquare\tcube") 


for number in numbers:
    square = number ** 2    
    cube = number ** 3      
    print(f"{number}\t{square}\t{cube}") 
