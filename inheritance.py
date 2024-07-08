class person:
    def __init__(self, fname, lname):
        self.firstname=fname
        self.lastname=lname

    def printname(self):
        print(self.firstname, self.lastname)

x=person("jo","b")
x.printname()

#child class:
class student(person):
    pass

x=student("thanasis","the cat")
x.printname()
