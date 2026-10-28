"""
Question 12: Write a Python function that accepts a string and counts the number of upper and lower case letters.
"""


def count_case(text):
    upper = 0
    lower = 0
    for ch in text:
        if ch.isupper():
            upper = upper + 1
        elif ch.islower():
            lower = lower + 1
    print("Uppercase letters:", upper)
    print("Lowercase letters:", lower)


s = input("Enter a string: ")
count_case(s)
