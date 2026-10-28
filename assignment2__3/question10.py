"""
Question 10: Write a Python program that takes two numbers as input and compares them. Print whether the first number is greater than, less than, or equal to the second number.
"""

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

if num1 > num2:
    print(num1, "is greater than", num2)
elif num1 < num2:
    print(num1, "is less than", num2)
else:
    print(num1, "is equal to", num2)
