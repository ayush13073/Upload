import re

text = """
The examination will be conducted on 15/10/2026.
The project submission date is 25/10/2026.
"""

pattern = r"\b[0-9]{2}/[0-9]{2}/[0-9]{4}\b"

dates = re.findall(pattern, text)

print("Dates found:")
for date in dates:
    print(date)
