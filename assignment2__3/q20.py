students = {
    "Ravi":  {"height": 170, "width": 60},
    "Priya": {"height": 155, "width": 50},
    "Anil":  {"height": 180, "width": 75},
    "Sita":  {"height": 160, "width": 55},
    "Kiran": {"height": 175, "width": 65}
}

filtered = {}

for name in students:
    if students[name]["height"] >= 165 and students[name]["width"] >= 55:
        filtered[name] = students[name]

print("Students with height >= 165 and width >= 55 : ")
for name in filtered:
    print("%-8s height = %d , width = %d" % (name, filtered[name]["height"], filtered[name]["width"]))

    