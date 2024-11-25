def get_prime_number(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return True
    return False
    raise TypeError

