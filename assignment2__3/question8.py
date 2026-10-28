"""
Question 8: Write a Python program that converts temperature from Celsius to Fahrenheit and vice versa. The program should ask the user for the temperature value and the unit (Celsius or Fahrenheit) and then perform the conversion.
"""

value = float(input("Enter the temperature value: "))
unit = input("Enter the unit (C or F): ")

if unit == "C" or unit == "c":
    fahrenheit = (value * 9 / 5) + 32
    print(value, "Celsius =", fahrenheit, "Fahrenheit")
elif unit == "F" or unit == "f":
    celsius = (value - 32) * 5 / 9
    print(value, "Fahrenheit =", celsius, "Celsius")
else:
    print("Invalid unit")
