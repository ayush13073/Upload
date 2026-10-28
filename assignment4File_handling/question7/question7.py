"""
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
