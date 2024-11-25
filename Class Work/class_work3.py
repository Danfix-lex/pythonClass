number = int(input("Enter your number: "))

def is_prime(number):
    if number <= 1:
        return False
    for num in range(2, int(number ** 0.5) + 1):
        if number % num == 0:
            return False
    return True

if is_prime(number):
    print(number, "is a prime")
else:
    print(number, "is not prime")

