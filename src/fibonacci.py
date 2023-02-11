def fibonacci(n, memo=None):
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 0:
        return 0
    if n <= 2:
        return 1

    memo[n] = fibonacci(n - 1) + fibonacci(n - 2)

    return memo[n]
