class Animal:
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        print("Dog sounds bowww")

class Cat(Animal):
    def sound(self):
        print("Cat sounds meoww")

for v in [Dog(),Cat()]:
    v.sound()