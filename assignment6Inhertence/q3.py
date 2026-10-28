class Student:
    def __init__(self,name):
        self.name = name
    
class Course:
    def __init__(self,coursename,fees):
        self.coursename = coursename
        self.fees = fees

class courses(Student, Course):
    def __init__(self, name,coursename,fees):
        Student.__init__(self,name)
        Course.__init__(self,coursename,fees)


    def enroll(self):
        print(f"{self.name} {self.coursename} {self.fees}")


cs = courses("Ravi", "cs", 34)
cs.enroll()