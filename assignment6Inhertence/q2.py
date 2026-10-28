class Student:
    def __init__(self,name):
        self.name = name
    def setname(self, name):
        self.name = name
    def displayname(self):
        print(f"{self.name}")

class Test(Student):
    def __init__(self,name):
        Student.__init__(self,name)
        self.marks = []

    def setmarks(self,marks):
        self.marks = marks

    def displaymarks(self):
        print(f"{self.marks}")

class Marks(Test):
    def cala(self):
        total = 0

        for m in self.marks:
            total = total + m

        avg = total / len(self.marks)
        return avg


    def printc(self):
        avg = self.cala()


    def displaya(self):
        self.displayname()
        self.displaymarks()
        self.printc()

s = Marks("ayush")
s.setmarks([70,70,70])
s.displaya()