def factorial(n):
    if n < 0:
        return None

    if n == 0 or n == 1:
        return 1

    factorial = 1

    for x in range(1, n + 1):
        factorial = factorial * x

    return factorial
