# https://drive.google.com/drive/folders/173I1fVSeFK6bJL88liYzTLOgyJqQy8kO


def factorial(n):
    if n < 0:
        return None

    if n == 0 or n == 1:
        return 1

    factorial = 1
    for x in range(1, n + 1):
        factorial = factorial * x

    return factorial


try:
    number = int(input("Enter a positive integer number: "))
    factorial = factorial(number)
    print(f"The factorial of {number} is {factorial}")
except:
    print("Not a number")
