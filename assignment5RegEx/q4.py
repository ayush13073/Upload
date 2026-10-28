import re

text = """
Visit our website https://www.college.edu for details.
Also check http://library.college.edu/books
and https://github.com/example/repo
"""

pattern = r"https?://[^\s]+"

urls = re.findall(pattern, text)

print("URLs found:")
for url in urls:
    print(url)
