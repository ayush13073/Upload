filename = "sample.txt"
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
