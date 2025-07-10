class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def getname(self):
        print(self.name)

    def getage(self):
        print(self.age)

s1 = Student('Bhargavi',21)
s1.getname()
s1.getage()