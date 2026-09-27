# Program 1: Factorial of a Number
# Iterative and Recursive

def factorial_iterative(n):
    result = 1

    for i in range(1, n + 1):
        result = result * i

    return result


def factorial_recursive(n):
    if n == 0 or n == 1:
        return 1

    return n * factorial_recursive(n - 1)


n = int(input("Enter a number: "))

if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print("Factorial using iterative method:", factorial_iterative(n))
    print("Factorial using recursive method:", factorial_recursive(n))
