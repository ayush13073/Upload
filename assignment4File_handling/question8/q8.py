key = 23
tag = b"ENC:"

filename = input("Enter file name : ")
mode = input("Type 'e' or 'd' : ")

with open(filename, "rb") as file:
    data = file.read()

is_encrypted = data[:4] == tag