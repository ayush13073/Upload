"""
Question 16: Write a Python program to extract year, month, date and time using Lambda.
"""

from datetime import datetime

now = datetime.now()

extract = lambda dt: (dt.year, dt.month, dt.day, dt.hour, dt.minute, dt.second)

year, month, day, hour, minute, second = extract(now)

print("Year:", year)
print("Month:", month)
print("Date:", day)
print("Time:", hour, ":", minute, ":", second)
