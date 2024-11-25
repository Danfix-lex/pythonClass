number = int(input("Enter your number: "))
def get_number(number):
    dividerOne = 1
    dividerTwo = number - 1
    if number % dividerOne and number % dividerTwo and number != 0:
        print(number,": is a prime")
    
    else:
            print(number,": is not prime")

get_number(number)

