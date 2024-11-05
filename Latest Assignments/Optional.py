for i in range(10):
    number = int(input("Enter an integer: "))
    print("You entered: ", number)
    
    
    if number == 0:
        break
else:
    print("The loop stopped without executing the break")
