def get_prime_factors(number):
    if number < 1:
        return []
    if number <= 3:
        return [number]

    prime_factors = []
    divisor = 2

    while number > 1:
        while number % divisor == 0:
            number = number // divisor
            prime_factors.append(divisor)

        divisor = divisor + 1

    return prime_factors
