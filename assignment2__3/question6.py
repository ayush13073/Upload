"""
Question 6: Write a Python program that takes the principal amount, rate of interest, and time period as inputs and calculates the simple interest. Display the calculated interest.
"""

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period: "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest =", simple_interest)
