import re

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
