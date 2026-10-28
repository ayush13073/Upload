import os

for i in range(1, 9):
    os.makedirs("question" + str(i), exist_ok=True)


def write_file(path, content, newline=None):
    with open(path, "w", encoding="utf-8", newline=newline) as f:
        f.write(content)
    print("Created", path)


write_file("question1/sample.txt", """Python is a popular programming language.
Python is easy to learn and use.
Many people love Python programming.
Data science uses Python a lot.
""")

lines = ""
for i in range(1, 21):
    lines = lines + "Line " + str(i) + ": This is sample line number " + str(i) + ".\n"
write_file("question2/sample.txt", lines)

write_file("question3/file1.txt", "This is file one.\n")
write_file("question3/file2.txt", "This is file two.\n")
write_file("question3/file3.txt", "This is file three.\n")

write_file("question4/students.csv",
           "Name,City,Marks\nRiya,Pune,80\nSiya,Nashik,85\nKrish,Nagpur,75\n",
           newline="")

try:
    import pandas as pd
    df = pd.DataFrame({
        "Name": ["Riya", "Siya", "Krish"],
        "City": ["Pune", "Nashik", "Nagpur"],
        "Marks": [80, 85, 75]
    })
    df.to_excel("question5/students.xlsx", index=False)
    print("Created question5/students.xlsx")
except Exception:
    write_file("question5/students.csv",
               "Name,City,Marks\nRiya,Pune,80\nSiya,Nashik,85\nKrish,Nagpur,75\n",
               newline="")

large = ""
for i in range(1, 31):
    large = large + "This is line number " + str(i) + " of the large file.\n"
write_file("question7/large_file.txt", large)

write_file("question8/secret.txt",
           "This is a confidential message that must be protected.\n")

print("NOTE: Put your screenshot image in question6 folder and name it photo.png")
print("All folders and data files are ready.")


write_file("question1/question1.py", r'''"""
Question 1: Count below contents in file.
a. Count each letter Frequency in file
b. Words
c. Occurrences of specific words
d. Find longest word in file
"""

with open("sample.txt", "r") as f:
    text = f.read()

freq = {}
for ch in text:
    if ch.isalpha():
        ch = ch.lower()
        if ch in freq:
            freq[ch] = freq[ch] + 1
        else:
            freq[ch] = 1

print("Letter frequencies:")
for ch in freq:
    print(ch, ":", freq[ch])

words = text.split()
print("Total words:", len(words))

search = input("Enter word to search: ")
count = 0
for w in words:
    if w.lower() == search.lower():
        count = count + 1
print("Occurrences of", search, ":", count)

longest = ""
for w in words:
    if len(w) > len(longest):
        longest = w
print("Longest word:", longest)
''')


write_file("question2/question2.py", r'''"""
Question 2: Read specific file content as mention below.
a. Read first n no of lines
b. Read last n no of lines
c. Read specific n no of lines
"""

n = int(input("Enter n: "))

with open("sample.txt", "r") as f:
    all_lines = f.readlines()

print("First", n, "lines:")
count = 0
for line in all_lines:
    if count == n:
        break
    print(line.rstrip())
    count = count + 1

print("Last", n, "lines:")
for line in all_lines[-n:]:
    print(line.rstrip())

start = int(input("Enter start line number: "))
end = int(input("Enter end line number: "))

print("Lines from", start, "to", end, ":")
for line in all_lines[start - 1:end]:
    print(line.rstrip())
''')


write_file("question3/question3.py", r'''"""
Question 3: Using Switch case perform following.
a. Rename a multiple file with prefix
b. Copy file using Binary code
c. List all files in directory and save
"""

import os

print("1. Rename all .txt files with prefix")
print("2. Copy file using binary mode")
print("3. List all files and save to a file")
choice = input("Enter your choice (1-3): ")

if choice == "1":
    prefix = input("Enter prefix: ")
    for name in os.listdir("."):
        if name.endswith(".txt"):
            os.rename(name, prefix + name)
            print("Renamed", name, "to", prefix + name)

elif choice == "2":
    source = input("Enter source file name: ")
    destination = input("Enter destination file name: ")
    with open(source, "rb") as f:
        data = f.read()
    with open(destination, "wb") as f:
        f.write(data)
    print("Copied", source, "to", destination)

elif choice == "3":
    names = os.listdir(".")
    with open("file_list.txt", "w") as f:
        for name in names:
            f.write(name + "\n")
    print("Directory list saved in file_list.txt")

else:
    print("Invalid choice")
''')


write_file("question4/question4.py", r'''"""
Question 4: Read and write csv file which has following content in tabular format.

Name      City      Marks(out of 100)
Riya      Pune      80
Siya      Nashik    85
Krish     Nagpur    75
"""

import csv

print("Name       City       Marks")
print("-----------------------------")

with open("students.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row[0], "      ", row[1], "     ", row[2])

print("Adding one new student...")

with open("students.csv", "a", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["Aarav", "Mumbai", "90"])

print("Updated file:")
print("Name       City       Marks")
print("-----------------------------")

with open("students.csv", "r") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row[0], "      ", row[1], "     ", row[2])
''')


write_file("question5/question5.py", r'''"""
Question 5: Read excel file and display the result in tabular format.
Hint: import pandas and tabulate.
"""

import pandas as pd
from tabulate import tabulate

try:
    df = pd.read_excel("students.xlsx")
except Exception:
    df = pd.read_csv("students.csv")

print(tabulate(df, headers="keys", tablefmt="grid", showindex=False))
''')


write_file("question6/question6.py", r'''"""
Question 6: Read and write binary image file.

Before running this program, put an image file in this folder
and name it photo.png (or change the file name below).
"""

try:
    with open("photo.png", "rb") as f:
        data = f.read()

    print("Original image size:", len(data), "bytes")

    with open("copy.png", "wb") as f:
        f.write(data)

    print("Copy created as copy.png")

    with open("copy.png", "rb") as f:
        copy_data = f.read()

    print("Copy image size:", len(copy_data), "bytes")

    if data == copy_data:
        print("Both files are same")
    else:
        print("Files are different")

except FileNotFoundError:
    print("photo.png not found. Please put an image named photo.png in this folder.")
''')


write_file("question7/question7.py", r'''"""
Question 7: Split Large File into Smaller 10-Line Files.
"""

with open("large_file.txt", "r") as f:
    all_lines = f.readlines()

part = 1
start = 0

while start < len(all_lines):
    chunk = all_lines[start:start + 10]
    filename = "part" + str(part) + ".txt"
    with open(filename, "w") as f:
        for line in chunk:
            f.write(line)
    print("Created", filename, "with", len(chunk), "lines")
    start = start + 10
    part = part + 1

print("Total parts created:", part - 1)
''')


write_file("question8/question8.py", r'''"""
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
''')


print("All Assignment (File Handling) files generated successfully.")