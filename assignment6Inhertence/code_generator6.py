def write_file(path, content):
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)
    print("Created", path)


write_file("question1.py", r'''"""
Question 1: Create basic bank application with functionality deposit(), withdraw() and check_balance().
Base Class is Account with methods check_balance(), deposit(), withdraw().
Derived class is SavingAccount with method calculate_interest().
(Hint: Single Inheritance)
"""


class Account:
    def __init__(self, balance):
        self.balance = balance

    def check_balance(self):
        print("Balance:", self.balance)

    def deposit(self, amount):
        self.balance = self.balance + amount
        print("Deposited", amount, "New balance:", self.balance)

    def withdraw(self, amount):
        if amount > self.balance:
            print("Not enough balance")
        else:
            self.balance = self.balance - amount
            print("Withdrawn", amount, "New balance:", self.balance)


class SavingAccount(Account):
    def calculate_interest(self, rate):
        interest = self.balance * rate / 100
        print("Interest at", rate, "% =", interest)


account = SavingAccount(1000)
account.check_balance()
account.deposit(500)
account.withdraw(200)
account.calculate_interest(5)
''')


write_file("question2.py", r'''"""
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
''')


write_file("question3.py", r'''"""
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
''')


write_file("question4.py", r'''"""
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
''')


write_file("question5.py", r'''"""
Question 5: Hierarchical Inheritance.
Base class: Employee with method employee_details(EmpID, Name)
Derived class: Designer(Employee) with method designer_details(tool)
Derived class: Developer(Employee) with method developer_details(tool)
"""


class Employee:
    def employee_details(self, emp_id, name):
        print("Emp ID:", emp_id, "Name:", name)


class Designer(Employee):
    def designer_details(self, tool):
        print("Designer tool:", tool)


class Developer(Employee):
    def developer_details(self, tool):
        print("Developer tool:", tool)


designer = Designer()
designer.employee_details(1, "Riya")
designer.designer_details("Figma")

developer = Developer()
developer.employee_details(2, "Krish")
developer.developer_details("VS Code")
''')


write_file("question6.py", r'''"""
Question 6: Hybrid Inheritance.
Base class: Device with method device_details(DeviceID, Powered)
Derived class: Laptop with method laptop_details
Derived class: Mobile with method mobile_details
Derived class: SmartPhone(Laptop, Mobile) with method smartphone_details

Note: The question in the document was cut off after "Laptop", so this
program uses Laptop and Mobile as the two branches and SmartPhone as the
combined class to demonstrate hybrid inheritance.
"""


class Device:
    def device_details(self, device_id, powered):
        print("Device ID:", device_id, "Powered:", powered)


class Laptop(Device):
    def laptop_details(self, ram):
        print("Laptop RAM:", ram)


class Mobile(Device):
    def mobile_details(self, camera):
        print("Mobile camera:", camera)


class SmartPhone(Laptop, Mobile):
    def smartphone_details(self, model):
        print("SmartPhone model:", model)


phone = SmartPhone()
phone.device_details(101, True)
phone.laptop_details("8GB")
phone.mobile_details("48MP")
phone.smartphone_details("Galaxy")
''')


write_file("question7.py", r'''"""
Question 7: Method Overriding.
Base class: PaymentGateway with method process_payment(self, amount)
Derived class: CreditCardPayment(PaymentGateway) with method process_payment(self, amount)
Derived class: UPIPayment(PaymentGateway) with method process_payment(self, amount)
"""


class PaymentGateway:
    def process_payment(self, amount):
        print("Processing payment of", amount, "through generic gateway")


class CreditCardPayment(PaymentGateway):
    def process_payment(self, amount):
        print("Processing credit card payment of", amount)


class UPIPayment(PaymentGateway):
    def process_payment(self, amount):
        print("Processing UPI payment of", amount)


card = CreditCardPayment()
card.process_payment(500)

upi = UPIPayment()
upi.process_payment(300)
''')


write_file("question8.py", r'''"""
Question 8: Polymorphism.
Same method name sound() in different classes, called through a loop.
"""


class Dog:
    def sound(self):
        print("Dog says Woof")


class Cat:
    def sound(self):
        print("Cat says Meow")


class Cow:
    def sound(self):
        print("Cow says Moo")


animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.sound()
''')


write_file("question9.py", r'''"""
Question 9: Interface.
Define Shape as interface which forces all subclasses to implement area() method.
Define Circle and Triangle as classes which implement the Shape interface.
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


circle = Circle(5)
print("Circle area:", circle.area())

triangle = Triangle(4, 6)
print("Triangle area:", triangle.area())
''')


print("All Assignment 6 (Inheritance) files generated successfully.")