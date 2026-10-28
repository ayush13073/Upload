import csv

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
