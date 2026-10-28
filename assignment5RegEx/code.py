# codegenerator.py
# Run this once. It creates q1.py to q7.py with full code + sample values.

# ---------------- Q1 code ----------------
q1_code = r'''import re

mobile = input("Enter mobile number: ")

pattern = r"^[6-9][0-9]{9}$"

if re.fullmatch(pattern, mobile):
    print("Valid mobile number")
else:
    print("Invalid mobile number")
'''

# ---------------- Q2 code ----------------
q2_code = r'''import re

text = """
The examination will be conducted on 15/10/2026.
The project submission date is 25/10/2026.
"""

pattern = r"\b[0-9]{2}/[0-9]{2}/[0-9]{4}\b"

dates = re.findall(pattern, text)

print("Dates found:")
for date in dates:
    print(date)
'''

# ---------------- Q3 code ----------------
q3_code = r'''import re

text = """
Contact us at support@college.edu or admin@university.com.
For personal queries: ravi.sharma@gmail.com
"""

pattern = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"

emails = re.findall(pattern, text)

print("Email addresses:")
for email in emails:
    print(email)
'''

# ---------------- Q4 code ----------------
q4_code = r'''import re

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
'''

# ---------------- Q5 code ----------------
q5_code = r'''import re

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
'''

# ---------------- Q6 code ----------------
q6_code = r'''import re

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
'''

# ---------------- Q7 code ----------------
q7_code = r'''import re

text = """
Ravi (Roll: 101) email ravi@gmail.com mobile 9876543210.
Priya (Roll: 102) email priya@gmail.com mobile 8765432109.
Exam date: 20/11/2026. Results on 15/12/2026.
#Batch2026 #Toppers #ExamUpdate
"""

email_pattern   = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}"
mobile_pattern  = r"\b[6-9][0-9]{9}\b"
date_pattern    = r"\b[0-9]{2}/[0-9]{2}/[0-9]{4}\b"
roll_pattern    = r"Roll[:\s]+[0-9]+"
hashtag_pattern = r"#[A-Za-z0-9_]+"

emails   = re.findall(email_pattern, text)
mobiles  = re.findall(mobile_pattern, text)
dates    = re.findall(date_pattern, text)
rolls    = re.findall(roll_pattern, text)
hashtags = re.findall(hashtag_pattern, text)

print("Student Emails  :", emails)
print("Mobile Numbers  :", mobiles)
print("Dates           :", dates)
print("Roll Numbers    :", rolls)
print("Hashtags        :", hashtags)
'''

# ---------------- generate files (C-style) ----------------
names = ["q1.py", "q2.py", "q3.py", "q4.py", "q5.py", "q6.py", "q7.py"]
codes = [q1_code, q2_code, q3_code, q4_code, q5_code, q6_code, q7_code]

print("Generating files...")
print("")

i = 0
while i < len(names):
    with open(names[i], "w") as file:
        file.write(codes[i])
    print("  Created %s" % names[i])
    i = i + 1

print("")
print("Done. 7 files generated in this folder.")