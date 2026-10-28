class Employee:
    def __init__(self, emp_id, name):
        self.emp_id = emp_id
        self.name = name

    def Employee_Details(self):
        print("Emp ID = %d, Name = %s" % (self.emp_id, self.name))


class Designer(Employee):
    def __init__(self, emp_id, name, tool):
        Employee.__init__(self, emp_id, name)
        self.tool = tool

    def Designer_Details(self):
        print("Designer -> Tool = %s" % self.tool)


class Developer(Employee):
    def __init__(self, emp_id, name, tool):
        Employee.__init__(self, emp_id, name)
        self.tool = tool

    def Developer_Details(self):
        print("Developer -> Tool = %s" % self.tool)


d = Designer(101, "Ravi", "Photoshop")
v = Developer(102, "Priya", "VS Code")

print("=== Designer ===")
d.Employee_Details()
d.Designer_Details()

print("")
print("=== Developer ===")
v.Employee_Details()
v.Developer_Details()