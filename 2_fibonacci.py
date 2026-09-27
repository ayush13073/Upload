# Program 2: Nth Fibonacci Number
# Iterative and Recursive

def fibonacci_iterative(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    a = 0
    b = 1

    for i in range(2, n + 1):
        c = a + b
        a = b
        b = c

    return b


def fibonacci_recursive(n):
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


n = int(input("Enter n: "))

if n < 0:
    print("Please enter a non-negative number.")
else:
    print("Nth Fibonacci number using iterative method:",
          fibonacci_iterative(n))

    print("Nth Fibonacci number using recursive method:",
          fibonacci_recursive(n))
