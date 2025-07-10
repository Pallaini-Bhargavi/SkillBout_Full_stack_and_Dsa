class Demo:
    def show(self,a=None,b=None,c=None):
        if a and b and c:
            print("3 arg")

        elif (a and b):
            print("2 arg")

        elif a or b or c:
            print("1 arg")

        else:
            print("no arg")

d = Demo()
d.show(1,3,5)
d.show(1,2)
d.show(1)