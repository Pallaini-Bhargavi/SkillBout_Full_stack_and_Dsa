class Marks:
    def __init__(self):
        self.marks = []

    def add_mark(self,mark):
        self.marks.append(mark)

    def get_marks(self):
        return self.marks

m1 = Marks()
m1.add_mark(98)
m1.add_mark(80)
m1.add_mark(89)
m1.add_mark(92)
print(m1.get_marks())