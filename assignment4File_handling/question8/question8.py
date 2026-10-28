"""
Question 8: Data Security in File Handling.
This program encrypts the file content, saves it, then decrypts it back.
"""


def encrypt(text, shift):
    result = ""
    for ch in text:
        if ch.isupper():
            result = result + chr((ord(ch) - 65 + shift) % 26 + 65)
        elif ch.islower():
            result = result + chr((ord(ch) - 97 + shift) % 26 + 97)
        else:
            result = result + ch
    return result


with open("secret.txt", "r") as f:
    original = f.read()

encrypted = encrypt(original, 3)
with open("encrypted.txt", "w") as f:
    f.write(encrypted)

with open("encrypted.txt", "r") as f:
    stored = f.read()

decrypted = encrypt(stored, -3)
with open("decrypted.txt", "w") as f:
    f.write(decrypted)

print("Original :", original.rstrip())
print("Encrypted:", encrypted.rstrip())
print("Decrypted:", decrypted.rstrip())

if original == decrypted:
    print("Data recovered successfully")
else:
    print("Data does not match")
