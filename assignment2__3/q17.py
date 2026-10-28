n  = int(input("Enter n  : "))

student = []

i = 0

while(i < n):
    name =input(f"Enter name {i + 1} :  ")
    marks =int(input(f"enter marks { i + 1} : "))
    student.append([name, marks])
    i = i + 1

marks = []

for s in student:
    marks.append(s[1])

unique = list(set(marks))
unique.sort()

second = unique[1]

if (len(unique) < 2):
    print("not enough information ")
else:
    second = unique[1]
    names = []
    
    for s in student:
        if(s[1] == second):
            names.append(s[0])
        
    names.sort()
    print(f"second lowest marks is {second}")
    for s in names:
        print(s)


