"""
Question 3: Create Student Enrollment application.
Base class: Student with __init__ method with self, name
Base class: Course with name, course
Derived class: CourseStudent with enroll method
(Hint: Multiple Inheritance)
"""


class Student:
    def __init__(self, name):
        self.name = name


class Course:
    def __init__(self, course_name):
        self.course_name = course_name


class CourseStudent(Student, Course):
    def __init__(self, name, course_name):
        Student.__init__(self, name)
        Course.__init__(self, course_name)

    def enroll(self):
        print(self.name, "enrolled in", self.course_name)


student = CourseStudent("Riya", "Python")
student.enroll()
