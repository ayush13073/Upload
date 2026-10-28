"""
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

emails = re.findall(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", text)
phones = re.findall(r"\b[6-9]\d{9}\b", text)
urls = re.findall(r"https?://[A-Za-z0-9./_-]+", text)
dates = re.findall(r"\b\d{2}/\d{2}/\d{4}\b", text)
numbers = re.findall(r"\b\d+\b", text)
hashtags = re.findall(r"#\w+", text)

print("Email addresses:", emails)
print("Phone numbers:", phones)
print("URLs:", urls)
print("Dates:", dates)
print("Numbers:", numbers)
print("Hashtags:", hashtags)
