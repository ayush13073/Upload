"""
Question 3: Write a program to extract all email addresses from a paragraph.
"""

import re

text = """
You can contact us at support@example.com or sales@company.org.
For personal queries, email john.doe123@gmail.com.
"""

pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

emails = re.findall(pattern, text)

print("Email addresses:")
for email in emails:
    print(email)
