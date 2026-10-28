"""
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
