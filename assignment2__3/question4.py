"""
Question 4: Write a Python program that takes the length and width of a rectangle as input and calculates its area and perimeter. Display the results.
"""

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = length * width
perimeter = 2 * (length + width)

print("Area =", area)
print("Perimeter =", perimeter)
