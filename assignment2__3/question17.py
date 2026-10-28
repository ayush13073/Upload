num_students = int(input("Enter number of students: "))
students = []
i = 0
while i < num_students:
    name = input("  Name  : ")
    marks = int(input("  Marks : "))
    students.append([name, marks])
    i = i + 1

marks_list = []
for s in students:
    marks_list.append(s[1])

unique_marks = list(set(marks_list))
unique_marks.sort()

if len(unique_marks) < 2:
    print("Not enough different marks")
else:
    second_lowest = unique_marks[1]
    
    names = []
    for s in students:
        if s[1] == second_lowest:
            names.append(s[0])
            
    names.sort()
    
    print("Second lowest marks = %d" % second_lowest)
    for name in names:
        print(name)