class Academic:
    def academic_details(self, roll_no, marks):
        self.roll_no_academic = roll_no
        self.marks = marks

    def show_academic(self):
        print("Academic -> Roll No = %d, Marks = %d" %
              (self.roll_no_academic, self.marks))


class Sports:
    def sports_details(self, roll_no, marks):
        self.roll_no_sports = roll_no
        self.sports_marks = marks

    def show_sports(self):
        print("Sports   -> Roll No = %d, Marks = %d" %
              (self.roll_no_sports, self.sports_marks))


class Student(Academic, Sports):
    def student_details(self, roll_no, name):
        self.roll_no = roll_no
        self.name = name

    def show_student(self):
        print("Student  -> Roll No = %d, Name = %s" %
              (self.roll_no, self.name))


s = Student()
s.academic_details(101, 85)
s.sports_details(101, 90)
s.student_details(101, "Ravi")

print("")
s.show_academic()
s.show_sports()
s.show_student()