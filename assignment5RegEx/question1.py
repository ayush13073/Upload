# """
# Question 1: Write a program to validate a mobile number.
# Assume the mobile number must contain 10 digits and start with 6-9.
# """

# import re

# mobile = input("Enter mobile number: ")

# pattern = r"^[6-9]\d{9}$"

# if re.fullmatch(pattern, mobile):
#     print("Valid mobile number")
# else:
#     print("Invalid mobile number")













import re

mobile = input("Enter mobile number : ")

pattern = r"^[6-9][0-9]{9}$"

if re.fullmatch(pattern,mobile) :
    print("valid ")
else:
    print("invalid")