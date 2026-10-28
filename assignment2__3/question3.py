"""
Question 3: Create a simple calculator that allows the user to input two numbers and an operator (+, -, *, /, %, **, //). Based on the operator provided, the program should perform the corresponding arithmetic operation and display the result.
"""

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
operator = input("Enter an operator (+, -, *, /, %, **, //): ")

if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
elif operator == "%":
    result = num1 % num2
elif operator == "**":
    result = num1 ** num2
elif operator == "//":
    result = num1 // num2
else:
    result = None
    print("Invalid operator")

if result is not None:
    print("Result:", result)
