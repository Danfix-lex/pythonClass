def get_prime_number(number):
    prime_number = 0
    if number / number == 1 and number % 2 == 1:
        prime_number += number
        if prime_number == number:
            return True
        else:
            return False
        raise TypeError
        

number = 7
prime_number = get_prime_number(number)
print(prime_number)
