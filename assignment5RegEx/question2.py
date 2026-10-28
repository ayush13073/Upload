"""
Question 2: Extract dates from text.
"""

import re

text = """
The examination will be conducted on 15/10/2026.
The project submission date is 25/10/2026.
"""

pattern = r"\b\d{2}/\d{2}/\d{4}\b"

dates = re.findall(pattern, text)

print("Dates found:")
for date in dates:
    print(date)
