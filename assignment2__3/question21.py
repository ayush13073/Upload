"""
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
