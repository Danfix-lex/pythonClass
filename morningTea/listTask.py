def get_prime_number(numbers):
    prime_numbers = []
    for number in range(2, numbers+1):
        if number % 2 == 0:
            prime_numbers.append(number)
        return prime_numbers
        

numbers = []
prime_numbers = get_prime_number(numbers)
print(prime_numbers)
