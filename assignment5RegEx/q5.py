import re

text = """
Ravi's email is ravi@gmail.com and phone is 9876543210.
The event is on 15/10/2026. Visit https://college.edu for info.
Total fees: 50000. #CollegeFest #2026 #Python
"""

email_pattern   = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
phone_pattern   = r"\b[6-9][0-9]{9}\b"
url_pattern     = r"https?://[^\s]+"
date_pattern    = r"\b[0-9]{2}/[0-9]{2}/[0-9]{4}\b"
number_pattern  = r"\b[0-9]+\b"
hashtag_pattern = r"#[A-Za-z0-9_]+"

emails   = re.findall(email_pattern, text)
phones   = re.findall(phone_pattern, text)
urls     = re.findall(url_pattern, text)
dates    = re.findall(date_pattern, text)
numbers  = re.findall(number_pattern, text)
hashtags = re.findall(hashtag_pattern, text)

print("Emails   :", emails)
print("Phones   :", phones)
print("URLs     :", urls)
print("Dates    :", dates)
print("Numbers  :", numbers)
print("Hashtags :", hashtags)
