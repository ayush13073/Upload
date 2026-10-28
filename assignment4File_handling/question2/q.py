with open("sample.txt","r") as file:
    lines = file.readlines()

n = int(input("Enter how many lines : "))

print()

print("first %d lines" %n)

i = 0

while i < n and i < len(lines):
    print(lines[i], end = "")
    i = i + 1

    
i = len(lines) -n

if i < 0:
    i = 0
while i < len(lines):
    print(lines[i], end ="")
    i = i + 1


start  = int(input("start from line number "))
print("lines from line ")

i = start - 1

end = i + n

if end > len(lines):
    end = len(lines)

while i < end:
    print(lines[i], end ="")
    i = i + 1