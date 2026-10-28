"""
Question 2: Create Student application to set student and mark details and display all student details.
Base class: Student
Derived1 class: Test (get and set marks of student)
Derived2 class: Marks (calculate average and print class of students)
(Hint: Multilevel Inheritance)
"""


class Student:
    def __init__(self, name, roll):
        self.name = name
        self.roll = roll

    def show_student(self):
        print("Name:", self.name, "Roll:", self.roll)


class Test(Student):
    def __init__(self, name, roll):
        Student.__init__(self, name, roll)
        self.marks = []

    def set_marks(self, marks):
        self.marks = marks

    def get_marks(self):
        return self.marks


class Marks(Test):
    def average(self):
        total = 0
        for m in self.marks:
            total = total + m
        return total / len(self.marks)

    def print_class(self):
        avg = self.average()
        print("Average:", avg)
        if avg >= 75:
            print("Class: Distinction")
        elif avg >= 60:
            print("Class: First Class")
        elif avg >= 40:
            print("Class: Pass")
        else:
            print("Class: Fail")


student = Marks("Riya", 1)
student.show_student()
student.set_marks([80, 85, 90])
print("Marks:", student.get_marks())
student.print_class()
