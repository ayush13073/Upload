"""
Question 4: Multiple Inheritance - Create Academic application.
Base class: Academic with method academic_details(Roll_no, Marks)
Base class: Sports with method sports_details(Roll_no, Marks)
Derived class: Student(Academic, Sports) with method student_details(Roll_no, Name)
"""


class Academic:
    def academic_details(self, roll_no, marks):
        print("Academic - Roll:", roll_no, "Marks:", marks)


class Sports:
    def sports_details(self, roll_no, marks):
        print("Sports - Roll:", roll_no, "Marks:", marks)


class Student(Academic, Sports):
    def student_details(self, roll_no, name):
        print("Student - Roll:", roll_no, "Name:", name)


student = Student()
student.student_details(1, "Riya")
student.academic_details(1, 85)
student.sports_details(1, 90)
