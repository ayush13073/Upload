import re

text = """
Contact us at support@college.edu or admin@university.com.
For personal queries: ravi.sharma@gmail.com
"""

pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

emails = re.findall(pattern, text)

print("Email addresses:")
for email in emails:
    print(email)
