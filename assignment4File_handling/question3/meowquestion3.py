"""
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
