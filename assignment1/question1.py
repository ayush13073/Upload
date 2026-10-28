"""
Question 1: Create a menu-driven program using a while loop:
- Factorial
- Prime Check
- Fibonacci Series
- Reverse Number
- Exit
"""


def factorial(n):
    if n < 0:
        return None
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def is_prime(n):
    if n < 2:
        return False
    divisor = 2
    while divisor * divisor <= n:
        if n % divisor == 0:
            return False
        divisor += 1
    return True


def fibonacci(terms):
    series = []
    first, second = 0, 1
    for _ in range(terms):
        series.append(first)
        first, second = second, first + second
    return series


def reverse_number(n):
    negative = n < 0
    n = abs(n)
    reversed_value = 0
    while n > 0:
        reversed_value = reversed_value * 10 + n % 10
        n //= 10
    return -reversed_value if negative else reversed_value


def main():
    while True:
        print("\n----- MENU -----")
        print("1. Factorial")
        print("2. Prime Check")
        print("3. Fibonacci Series")
        print("4. Reverse Number")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == "1":
            n = int(input("Enter a number: "))
            value = factorial(n)
            if value is None:
                print("Factorial is not defined for negative numbers.")
            else:
                print(f"Factorial of {n} = {value}")

        elif choice == "2":
            n = int(input("Enter a number: "))
            if is_prime(n):
                print(f"{n} is a prime number.")
            else:
                print(f"{n} is not a prime number.")

        elif choice == "3":
            terms = int(input("Enter the number of terms: "))
            if terms <= 0:
                print("Please enter a positive number of terms.")
            else:
                print("Fibonacci Series:", " ".join(str(x) for x in fibonacci(terms)))

        elif choice == "4":
            n = int(input("Enter a number: "))
            print(f"Reverse of {n} = {reverse_number(n)}")

        elif choice == "5":
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please select a valid option.")


if __name__ == "__main__":
    main()
