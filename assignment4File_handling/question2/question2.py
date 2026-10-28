"""
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
