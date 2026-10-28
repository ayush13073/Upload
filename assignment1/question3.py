"""
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
