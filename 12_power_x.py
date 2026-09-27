def power_iterative(x, n):
    result = 1

    for i in range(n):
        result = result * x

    return result


def power_recursive(x, n):
    if n == 0:
        return 1

    return x * power_recursive(x, n - 1)


x = int(input("Enter x: "))
n = int(input("Enter n: "))

if n < 0:
    print("Please enter a non-negative exponent.")
else:
    print("x^n using iterative method:", power_iterative(x, n))
    print("x^n using recursive method:", power_recursive(x, n))
