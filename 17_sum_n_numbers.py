def sum_iterative(n):
    sum = 0

    for i in range(1, n + 1):
        sum = sum + i

    return sum


def sum_recursive(n):
    if n == 0:
        return 0

    return n + sum_recursive(n - 1)


n = int(input("Enter n: "))

if n < 0:
    print("Please enter a non-negative number.")
else:
    print("Sum using iterative method:", sum_iterative(n))
    print("Sum using recursive method:", sum_recursive(n))
