"""
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
