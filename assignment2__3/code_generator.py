import os

files = {}

files["question1.py"] = '''"""
Question 1: Create variables of different data types (string, integer, float, Boolean) and print their values and types.
"""

name = "Alice"
age = 20
height = 5.6
is_student = True

print("Value:", name, "Type:", type(name))
print("Value:", age, "Type:", type(age))
print("Value:", height, "Type:", type(height))
print("Value:", is_student, "Type:", type(is_student))
'''

files["question2.py"] = '''"""
Question 2: Write a Python program that asks the user for their name and age, then prints a message saying "Hello, [Name]! You are [Age] years old."
"""

name = input("Enter your name: ")
age = input("Enter your age: ")

print("Hello, " + name + "! You are " + age + " years old.")
'''

files["question3.py"] = '''"""
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
'''

files["question4.py"] = '''"""
Question 4: Write a Python program that takes the length and width of a rectangle as input and calculates its area and perimeter. Display the results.
"""

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

area = length * width
perimeter = 2 * (length + width)

print("Area =", area)
print("Perimeter =", perimeter)
'''

files["question5.py"] = '''"""
Question 5: Write a Python program that takes an integer as input and determines if it is even or odd. Print the result.
"""

number = int(input("Enter an integer: "))

if number % 2 == 0:
    print(number, "is even")
else:
    print(number, "is odd")
'''

files["question6.py"] = '''"""
Question 6: Write a Python program that takes the principal amount, rate of interest, and time period as inputs and calculates the simple interest. Display the calculated interest.
"""

principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time period: "))

simple_interest = (principal * rate * time) / 100

print("Simple Interest =", simple_interest)
'''

files["question7.py"] = '''"""
Question 7: Write a Python program that takes three numbers as input and calculates their average. Print the result.
"""

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

average = (num1 + num2 + num3) / 3

print("Average =", average)
'''

files["question8.py"] = '''"""
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
'''

files["question9.py"] = '''"""
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
'''

files["question10.py"] = '''"""
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
'''

files["question12.py"] = '''"""
Question 12: Write a Python function that accepts a string and counts the number of upper and lower case letters.
"""


def count_case(text):
    upper = 0
    lower = 0
    for ch in text:
        if ch.isupper():
            upper = upper + 1
        elif ch.islower():
            lower = lower + 1
    print("Uppercase letters:", upper)
    print("Lowercase letters:", lower)


s = input("Enter a string: ")
count_case(s)
'''

files["question13.py"] = '''"""
Question 13: Write a Python function that accepts a string and counts the number of upper and lower case letters.
"""


def count_case(text):
    upper = 0
    lower = 0
    for ch in text:
        if ch.isupper():
            upper = upper + 1
        elif ch.islower():
            lower = lower + 1
    print("Uppercase letters:", upper)
    print("Lowercase letters:", lower)


s = input("Enter a string: ")
count_case(s)
'''

files["question14.py"] = '''"""
Question 14: Write a Python program to create Fibonacci series up to n using Lambda.
"""

fib = lambda n: n if n <= 1 else fib(n - 1) + fib(n - 2)

terms = int(input("Enter the number of terms: "))

series = []
for i in range(terms):
    series.append(fib(i))

print("Fibonacci Series:", series)
'''

files["question15.py"] = '''"""
Question 15: Write a compose(f, g) utility function that returns a new function equivalent to applying g first and then f to the result — that is, compose(f, g)(x) should equal f(g(x)). Test it by composing a lambda that doubles a number with a lambda that adds.
"""


def compose(f, g):
    return lambda x: f(g(x))


double = lambda x: x * 2
add_one = lambda x: x + 1

combined = compose(double, add_one)

num = int(input("Enter a number: "))
print("Result:", combined(num))
'''

files["question16.py"] = '''"""
Question 16: Write a Python program to extract year, month, date and time using Lambda.
"""

from datetime import datetime

now = datetime.now()

extract = lambda dt: (dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)

year, month, day, hour, minute, second = extract(now)

print("Year:", year)
print("Month:", month)
print("Date:", day)
print("Time:", hour, ":", minute, ":", second)
'''

files["question17.py"] = '''"""
Question 17: Write a Python program to find the second lowest total marks of any student(s) from the given names and marks of each student using lists and lambda. Input the number of students, the names and grades of each student.
"""

n = int(input("Enter the number of students: "))

students = []
for i in range(n):
    name = input("Enter name: ")
    marks = float(input("Enter marks: "))
    students.append([name, marks])

students.sort(key=lambda x: x[1])

second_lowest_marks = students[1][1]

names = []
for student in students:
    if student[1] == second_lowest_marks:
        names.append(student[0])

print("Second lowest marks:", second_lowest_marks)
print("Student(s):", names)
'''

files["question20.py"] = '''"""
Question 20: Write a Python program to convert more than one list to a nested dictionary.
"""

keys = ["a", "b", "c"]
list1 = [1, 2, 3]
list2 = [10, 20, 30]

nested = {}

for i in range(len(keys)):
    nested[keys[i]] = {"list1": list1[i], "list2": list2[i]}

print(nested)
'''

files["question21.py"] = '''"""
Question 21: Write a Python program to filter the height and width of students, which are stored in a dictionary.
"""

students = {
    "Alice": {"height": 165, "width": 50},
    "Bob": {"height": 180, "width": 70},
    "Charlie": {"height": 170, "width": 60}
}

result = {}

for name in students:
    if students[name]["height"] >= 170 and students[name]["width"] >= 60:
        result[name] = students[name]

print("Filtered students:", result)
'''

files["question22.py"] = '''"""
Question 22: Write a Python program to remove the intersection of a second set with a first set.
"""

set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

set1 = set1 - set2

print("First set after removing intersection:", set1)
'''

files["question23.py"] = '''"""
Question 23: Write a Python program to find all the unique words and count the frequency of occurrence from a given list of strings. Use Python set data type.
"""

strings = ["hello world", "hello python", "world of python"]

words = []

for s in strings:
    for w in s.split():
        words.append(w)

unique_words = set(words)

for word in unique_words:
    count = words.count(word)
    print(word, ":", count)
'''

files["question24.py"] = '''"""
Question 24: Write a Python program to print a dictionary in table format.
"""

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Age": [25, 30, 35],
    "City": ["New York", "London", "Paris"]
}

print("Name       Age   City")
print("----------------------------")

for i in range(len(data["Name"])):
    print(data["Name"][i], "   ", data["Age"][i], "   ", data["City"][i])
'''

for filename, content in files.items():
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print("Created", filename)

print("All Assignment 2 files generated.")