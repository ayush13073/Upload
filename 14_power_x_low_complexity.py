def power(x, n):
    result = 1

    while n > 0:
        if n % 2 == 1:
            result = result * x

        x = x * x
        n = n // 2

    return result


x = int(input("Enter x: "))
n = int(input("Enter n: "))

if n < 0:
    print("Please enter a non-negative exponent.")
else:
    print("x^n:", power(x, n))
