"""
Question 7: Student Information Extractor Using Regular Expressions.

Develop a Python program that accepts a paragraph containing student information and extracts:
- Student email addresses
- Mobile numbers
- Dates
- Student roll numbers
- Hashtags
"""

import re

text = input("Enter a paragraph about students: ")

emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
mobiles = re.findall(r"\b[6-9]\d{9}\b", text)
dates = re.findall(r"\b\d{2}/\d{2}/\d{4}\b", text)
roll_numbers = re.findall(r"\bR\d{3,}\b", text)
hashtags = re.findall(r"#\w+", text)

print("Student email addresses:", emails)
print("Mobile numbers:", mobiles)
print("Dates:", dates)
print("Student roll numbers:", roll_numbers)
print("Hashtags:", hashtags)
