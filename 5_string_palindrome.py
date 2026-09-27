s = input("Enter a string: ")

reverse = ""
i = len(s) - 1

while i >= 0:
    reverse = reverse + s[i]
    i = i - 1

if s == reverse:
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")
