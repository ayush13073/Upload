"""
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
