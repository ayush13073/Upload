import re

password = input("Enter password: ")

has_length  = len(password) >= 8
has_upper   = re.search(r"[A-Z]", password)
has_lower   = re.search(r"[a-z]", password)
has_digit   = re.search(r"[0-9]", password)
has_special = re.search(r"[^A-Za-z0-9]", password)

if has_length and has_upper and has_lower and has_digit and has_special:
    print("Valid password")
else:
    print("Invalid password")
    if not has_length:
        print("  - must be at least 8 characters")
    if not has_upper:
        print("  - must contain an uppercase letter")
    if not has_lower:
        print("  - must contain a lowercase letter")
    if not has_digit:
        print("  - must contain a digit")
    if not has_special:
        print("  - must contain a special character")
