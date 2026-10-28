"""
Question 5: Write a Python program that takes an integer as input and determines if it is even or odd. Print the result.
"""

number = int(input("Enter an integer: "))

if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")
