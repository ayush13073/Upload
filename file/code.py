# codegenerator.py
# Run this ONCE. It creates:
#   sample.txt         (60 lines of real text)
#   q1.py .. q8.py     (each one runs on its own)

# =====================================================
# STEP 1: Write sample.txt (used by q1, q2, q7)
# =====================================================
sample_lines = []
i = 1
while i <= 60:
    sample_lines.append("Line %d of the sample file used in this assignment." % i)
    i = i + 1

# First 4 lines replaced with meaningful text for q1 counting
sample_lines[0] = "The quick brown fox jumps over the lazy dog."
sample_lines[1] = "Python is very easy to learn for beginners and students."
sample_lines[2] = "The teacher said the exam will be on the twenty fifth."
sample_lines[3] = "Regular expressions make text processing very simple and fast."

with open("sample.txt", "w") as file:
    for line in sample_lines:
        file.write(line + "\n")

print("Created sample.txt (60 lines)")
print("")

# =====================================================
# STEP 2: Q1 code
# =====================================================
q1_code = r'''filename = "sample.txt"

with open(filename, "r") as file:
    text = file.read()

# ---------- a) letter frequency (using isalpha) ----------
print("--- Letter frequency ---")
lower_text = text.lower()
done = ""
for ch in lower_text:
    if ch.isalpha() and ch not in done:
        count = 0
        for c in lower_text:
            if c == ch:
                count = count + 1
        print("%s = %d" % (ch, count))
        done = done + ch

# ---------- b) total words ----------
words = text.split()
print("")
print("--- Total words = %d ---" % len(words))

# ---------- c) occurrences of specific word ----------
search_word = "the"
count = 0
for w in words:
    if w.lower() == search_word:
        count = count + 1
print("--- '%s' appears %d times ---" % (search_word, count))

# ---------- d) longest word ----------
longest = ""
for w in words:
    if len(w) > len(longest):
        longest = w
print("")
print("--- Longest word = %s (length %d) ---" % (longest, len(longest)))
'''

# =====================================================
# STEP 3: Q2 code
# =====================================================
q2_code = r'''filename = "sample.txt"

with open(filename, "r") as file:
    lines = file.readlines()

n = 3
start = 5

print("--- File has %d lines ---" % len(lines))

# ---------- a) first n lines ----------
print("")
print("--- First %d lines ---" % n)
i = 0
while i < n and i < len(lines):
    print(lines[i], end="")
    i = i + 1

# ---------- b) last n lines ----------
print("")
print("--- Last %d lines ---" % n)
i = len(lines) - n
if i < 0:
    i = 0
while i < len(lines):
    print(lines[i], end="")
    i = i + 1

# ---------- c) n lines from a specific line number ----------
print("")
print("--- %d lines from line %d ---" % (n, start))
i = start - 1
end = i + n
if end > len(lines):
    end = len(lines)
while i < end:
    print(lines[i], end="")
    i = i + 1
'''

# =====================================================
# STEP 4: Q3 code (rename / copy / list - menu)
# =====================================================
q3_code = r'''import os

# ---------- setup: make test folder and files if missing ----------
if not os.path.exists("test_folder"):
    os.makedirs("test_folder")

if not os.path.exists("test_folder/file1.txt") and not os.path.exists("test_folder/new_file1.txt"):
    with open("test_folder/file1.txt", "w") as f:
        f.write("Hello from file1")
    with open("test_folder/file2.txt", "w") as f:
        f.write("Hello from file2")

print("1. Rename files with prefix")
print("2. Copy file (binary)")
print("3. List files and save")
print("4. Exit")
choice = int(input("Enter choice: "))

# ---------- a) rename with prefix ----------
if choice == 1:
    folder = "test_folder"
    prefix = "new_"

    for f in os.listdir(folder):
        old_path = os.path.join(folder, f)
        if os.path.isfile(old_path) and not f.startswith(prefix):
            new_name = prefix + f
            new_path = os.path.join(folder, new_name)
            os.rename(old_path, new_path)
            print("%s -> %s" % (f, new_name))

# ---------- b) copy file (binary) ----------
elif choice == 2:
    # pick any existing source - works no matter which option ran first
    if os.path.exists("test_folder/file1.txt"):
        source = "test_folder/file1.txt"
    elif os.path.exists("test_folder/new_file1.txt"):
        source = "test_folder/new_file1.txt"
    else:
        source = None

    if source is None:
        print("No source file found in test_folder")
    else:
        dest = "test_folder/copied.txt"
        with open(source, "rb") as src:
            with open(dest, "wb") as dst:
                while 1:
                    chunk = src.read(1024)
                    if chunk == b"":
                        break
                    dst.write(chunk)
        print("Copied %s -> %s" % (source, dest))

# ---------- c) list files and save ----------
elif choice == 3:
    folder = "test_folder"
    output = "test_folder/list.txt"

    with open(output, "w") as out:
        for f in os.listdir(folder):
            out.write(f + "\n")
            print(f)

    print("List saved to %s" % output)

elif choice == 4:
    print("Bye")

else:
    print("Invalid choice")
'''

# =====================================================
# STEP 5: Q4 code (CSV)
# =====================================================
q4_code = r'''import csv

# ---------- write CSV ----------
with open("students.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name", "City", "Marks"])
    writer.writerow(["Riya", "Pune", 80])
    writer.writerow(["Siya", "Nashik", 85])
    writer.writerow(["Krish", "Nagpur", 75])

print("CSV file written")
print("")

# ---------- read CSV ----------
with open("students.csv", "r") as file:
    reader = csv.reader(file)

    print("%-10s | %-10s | %-5s" % ("Name", "City", "Marks"))
    print("-" * 32)
    for row in reader:
        print("%-10s | %-10s | %-5s" % (row[0], row[1], row[2]))
'''

# =====================================================
# STEP 6: Q5 code (Excel + tabulate)
# =====================================================
q5_code = r'''import pandas as pd
from tabulate import tabulate

# ---------- write Excel ----------
data = {
    "Name":  ["Riya", "Siya", "Krish"],
    "City":  ["Pune", "Nashik", "Nagpur"],
    "Marks": [80, 85, 75]
}
df = pd.DataFrame(data)
df.to_excel("students.xlsx", index=False)
print("Excel file written")
print("")

# ---------- read Excel ----------
df2 = pd.read_excel("students.xlsx")

print(tabulate(df2, headers="keys", tablefmt="grid", showindex=False))
'''

# =====================================================
# STEP 7: Q6 code (binary image)
# =====================================================
q6_code = r'''import os

# ---------- create small binary file (fake PNG) if missing ----------
if not os.path.exists("input_image.bin"):
    with open("input_image.bin", "wb") as f:
        f.write(b"\x89PNG\r\n\x1a\n")
        for i in range(200):
            f.write(bytes([i % 256]))

print("Source binary file ready: input_image.bin")
print("")

# ---------- copy binary ----------
source = "input_image.bin"
dest   = "output_image.bin"

with open(source, "rb") as src:
    with open(dest, "wb") as dst:
        while 1:
            chunk = src.read(1024)
            if chunk == b"":
                break
            dst.write(chunk)

# ---------- verify sizes ----------
src_size = os.path.getsize(source)
dst_size = os.path.getsize(dest)

print("Copied %s -> %s" % (source, dest))
print("Source size = %d bytes" % src_size)
print("Dest   size = %d bytes" % dst_size)

if src_size == dst_size:
    print("Copy OK")
else:
    print("Copy FAILED")
'''

# =====================================================
# STEP 8: Q7 code (split file)
# =====================================================
q7_code = r'''filename = "sample.txt"
base = "chunk"

with open(filename, "r") as file:
    lines = file.readlines()

print("Source file %s has %d lines" % (filename, len(lines)))
print("")

part = 1
i = 0

while i < len(lines):
    part_name = base + "_" + str(part) + ".txt"

    with open(part_name, "w") as out:
        count = 0
        while count < 10 and i < len(lines):
            out.write(lines[i])
            i = i + 1
            count = count + 1

    print("Created %s (%d lines)" % (part_name, count))
    part = part + 1

print("")
print("Done. Created %d small files." % (part - 1))
'''

# =====================================================
# STEP 9: Q8 code (data security - auto encrypt/decrypt)
# =====================================================
q8_code = r'''import os

key = 42
tag = b"ENC:"
filename = "secret.txt"

# ---------- create demo file if missing ----------
if not os.path.exists(filename):
    with open(filename, "w") as f:
        f.write("This is a top secret message that needs protection.\n")
        f.write("Nobody should read this without the key.\n")
    print("Created demo file: %s" % filename)
    print("")

# ---------- read ----------
with open(filename, "rb") as file:
    data = file.read()

# ---------- decide: encrypt or decrypt ----------
if data[:4] == tag:
    # file has the tag -> already encrypted -> decrypt it
    inner = data[4:]
    new_list = []
    for byte in inner:
        new_list.append((byte - key) % 256)

    with open(filename, "wb") as file:
        file.write(bytes(new_list))

    print("File was ENCRYPTED -> now DECRYPTED")

else:
    # file has no tag -> normal -> encrypt it
    new_list = []
    for byte in data:
        new_list.append((byte + key) % 256)

    with open(filename, "wb") as file:
        file.write(tag + bytes(new_list))

    print("File was NORMAL -> now ENCRYPTED")
'''

# =====================================================
# STEP 10: Write all q*.py files
# =====================================================
names = ["q1.py", "q2.py", "q3.py", "q4.py",
         "q5.py", "q6.py", "q7.py", "q8.py"]

codes = [q1_code, q2_code, q3_code, q4_code,
         q5_code, q6_code, q7_code, q8_code]

print("Generating q*.py files...")
print("")

i = 0
while i < len(names):
    with open(names[i], "w") as file:
        file.write(codes[i])
    print("  Created %s" % names[i])
    i = i + 1

print("")
print("All done. Files on disk:")
print("  sample.txt  +  q1.py .. q8.py")