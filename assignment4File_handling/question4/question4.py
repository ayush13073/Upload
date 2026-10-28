"""
Question 4: Read and write csv file which has following content in tabular format.

Name      City      Marks(out of 100)
Riya      Pune      80
Siya      Nashik    85
Krish     Nagpur    75
"""

import csv

print("Name       City       Marks")
print("-----------------------------")

with open("students.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row[0], "      ", row[1], "     ", row[2])

print("Adding one new student...")

with open("students.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Aarav", "Mumbai", "90"])

print("Updated file:")
print("Name       City       Marks")
print("-----------------------------")

with open("students.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row[0], "      ", row[1], "     ", row[2])
