import os

files = {}

files["question1.py"] = '''"""
Question 1: Write a program to validate a mobile number.
Assume the mobile number must contain 10 digits and start with 6-9.
"""

import re

mobile = input("Enter mobile number: ")

pattern = r"^[6-9]\\d{9}$"

if re.fullmatch(pattern, mobile):
    print("Valid mobile number")
else:
    print("Invalid mobile number")
'''

files["question2.py"] = '''"""
Question 2: Extract dates from text.
"""

import re

text = """
The examination will be conducted on 15/10/2026.
The project submission date is 25/10/2026.
"""

pattern = r"\\b\\d{2}/\\d{2}/\\d{4}\\b"

dates = re.findall(pattern, text)

print("Dates found:")
for date in dates:
    print(date)
'''

files["question3.py"] = '''"""
Question 3: Write a program to extract all email addresses from a paragraph.
"""

import re

text = """
You can contact us at support@example.com or sales@company.org.
For personal queries, email john.doe123@gmail.com.
"""

pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}"

emails = re.findall(pattern, text)

print("Email addresses:")
for email in emails:
    print(email)
'''

files["question4.py"] = '''"""
Question 4: Write a Python program to extract all URLs from a given paragraph.
"""

import re

text = """
Visit our website at https://www.example.com for more details.
You can also check http://blog.example.org/python-regex.
Another useful link is https://docs.python.org/3/library/re.html.
"""

pattern = r"https?://[A-Za-z0-9./_-]+"

urls = re.findall(pattern, text)

print("URLs found:")
for url in urls:
    print(url)
'''

files["question5.py"] = '''"""
Question 5: Text Information Extractor Using Regular Expressions.

Develop a Python program that accepts a large paragraph and extracts:
- Email addresses
- Phone numbers
- URLs
- Dates
- Numbers
- Hashtags
"""

import re

text = input("Enter a paragraph: ")

emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}", text)
phones = re.findall(r"\\b[6-9]\\d{9}\\b", text)
urls = re.findall(r"https?://[A-Za-z0-9./_-]+", text)
dates = re.findall(r"\\b\\d{2}/\\d{2}/\\d{4}\\b", text)
numbers = re.findall(r"\\b\\d+\\b", text)
hashtags = re.findall(r"#\\w+", text)

print("Email addresses:", emails)
print("Phone numbers:", phones)
print("URLs:", urls)
print("Dates:", dates)
print("Numbers:", numbers)
print("Hashtags:", hashtags)
'''

files["question6.py"] = '''"""
Question 6: Write a Python program to validate a password with the following requirements:
- At least 8 characters
- At least one uppercase letter
- At least one lowercase letter
- At least one digit
- At least one special character
"""

import re

password = input("Enter a password: ")

length_ok = len(password) >= 8
upper_ok = re.search(r"[A-Z]", password)
lower_ok = re.search(r"[a-z]", password)
digit_ok = re.search(r"[0-9]", password)
special_ok = re.search(r"[^A-Za-z0-9]", password)

if length_ok and upper_ok and lower_ok and digit_ok and special_ok:
    print("Valid password")
else:
    print("Invalid password")
    if not length_ok:
        print("- Password must be at least 8 characters long")
    if not upper_ok:
        print("- Password must contain at least one uppercase letter")
    if not lower_ok:
        print("- Password must contain at least one lowercase letter")
    if not digit_ok:
        print("- Password must contain at least one digit")
    if not special_ok:
        print("- Password must contain at least one special character")
'''

files["question7.py"] = '''"""
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

emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,}", text)
mobiles = re.findall(r"\\b[6-9]\\d{9}\\b", text)
dates = re.findall(r"\\b\\d{2}/\\d{2}/\\d{4}\\b", text)
roll_numbers = re.findall(r"\\bR\\d{3,}\\b", text)
hashtags = re.findall(r"#\\w+", text)

print("Student email addresses:", emails)
print("Mobile numbers:", mobiles)
print("Dates:", dates)
print("Student roll numbers:", roll_numbers)
print("Hashtags:", hashtags)
'''

for filename, content in files.items():
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)
    print("Created", filename)

print("All Assignment 4 files generated.")