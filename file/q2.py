filename = "sample.txt"

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
