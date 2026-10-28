filename = "large_file.txt"
base = "new"

with open(filename,"r") as file:
    lines = file.readlines()

i = 0
part = 1

while i < len(lines):
    newpart = base + "_new" + str(part) + ".txt"
    with open(newpart,"w") as out:
        count = 0

        while count < 10 and i < len(lines):
            out.write(lines[i])
            count = count + 1
            i = i + 1

    print("created %s (%d line)", (newpart, count))
    part = part + 1