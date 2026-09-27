# Program 3: Nth Prime Number
# Iterative and Recursive

def is_prime(n):
    if n < 2:
        return 0

    i = 2

    while i * i <= n:
        if n % i == 0:
            return 0
        i = i + 1

    return 1


def nth_prime_iterative(n):
    count = 0
    number = 1

    while count < n:
        number = number + 1

        if is_prime(number) == 1:
            count = count + 1

    return number


def nth_prime_recursive(n, number, count):
    number = number + 1

    if is_prime(number) == 1:
        count = count + 1

    if count == n:
        return number

    return nth_prime_recursive(n, number, count)


n = int(input("Enter n: "))

if n <= 0:
    print("Please enter a positive number.")
else:
    print("Nth prime number using iterative method:",
          nth_prime_iterative(n))

    print("Nth prime number using recursive method:",
          nth_prime_recursive(n, 1, 0))
