class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def work(self,designation):
        print(f"Name: {self.name},Salary: {self.salary},Designation: {designation}")

class Manager:
    def __init__(self, name):
        self.name = name

    def manage(self):
        print(f"Manager Name: {self.name}")
        e = Employee("Edmonds", 20000)
        e.work("Developer")
m = Manager("Manager1")
m.manage()