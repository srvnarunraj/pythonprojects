class parent:
    firstname = ""
    lastname = ""

    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class child(parent):
    def display(self):
        print(self.firstname, self.lastname)


obj = parent("Arun", "Raj")
obj1 = child()
obj1.display()
obj1.printname()