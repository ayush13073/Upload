"""
Question 9: Write a Python program that calculates the Body Mass Index (BMI) based on user input for weight (in kg) and height (in meters). The formula for BMI is weight / (height ** 2). Display the BMI and categorize it as underweight, normal weight, overweight, or obese.
"""

weight = float(input("Enter weight in kg: "))
height = float(input("Enter height in meters: "))

bmi = weight / (height ** 2)

print("BMI =", round(bmi, 2))

if bmi < 18.5:
    print("Category: Underweight")
elif bmi < 25:
    print("Category: Normal weight")
elif bmi < 30:
    print("Category: Overweight")
else:
    print("Category: Obese")
