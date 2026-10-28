students = {
    "Ravi":  20,
    "Priya": 22,
    "Anil":  21,
    "Sita":  19,
    "Kiran": 23
}

print("=" * 28)
print("%-12s | %-10s" % ("Name", "Age"))
print("=" * 28)

for name in students:
    print("%-12s | %-10d" % (name, students[name]))

print("=" * 28)