import os

files = {}

files["question1.py"] = '''"""
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
        print("\\n----- MENU -----")
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
'''

files["question2.py"] = '''"""
Question 2: Generate a multiplication matrix (10 x 10).
"""


def main():
    size = 10
    print("Multiplication Matrix (10 x 10):\\n")
    for i in range(1, size + 1):
        row = []
        for j in range(1, size + 1):
            row.append(f"{i * j:5d}")
        print("".join(row))


if __name__ == "__main__":
    main()
'''

files["question3.py"] = '''"""
Question 3: Calculate the GCD and LCM of two numbers using loops.
"""


def main():
    a = int(input("Enter the first number: "))
    b = int(input("Enter the second number: "))

    x, y = abs(a), abs(b)
    while y != 0:
        x, y = y, x % y
    gcd = x

    if gcd == 0:
        print("GCD and LCM are not defined for 0 and 0.")
        return

    lcm = abs(a * b) // gcd
    print(f"GCD of {a} and {b} = {gcd}")
    print(f"LCM of {a} and {b} = {lcm}")


if __name__ == "__main__":
    main()
'''

files["question4.py"] = '''"""
Question 4: Print Floyd's Triangle.
1
2 3
4 5 6
7 8 9 10
"""


def main():
    rows = int(input("Enter the number of rows: "))
    if rows <= 0:
        print("Please enter a positive number of rows.")
        return

    number = 1
    for i in range(1, rows + 1):
        row = []
        for _ in range(i):
            row.append(str(number))
            number += 1
        print(" ".join(row))


if __name__ == "__main__":
    main()
'''

files["question5.py"] = '''"""
Question 5: Find the sum and average of the first N natural numbers.
"""


def main():
    n = int(input("Enter the value of N: "))
    if n <= 0:
        print("Please enter a positive integer.")
        return

    total = 0
    for i in range(1, n + 1):
        total += i

    average = total / n
    print(f"Sum of the first {n} natural numbers = {total}")
    print(f"Average of the first {n} natural numbers = {average}")


if __name__ == "__main__":
    main()
'''

for filename, content in files.items():
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"Created {filename}")

print("All files generated successfully.")