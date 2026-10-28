"""
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
