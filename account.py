class Account:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        self.__balance = 0

    def display_balance(self, balance):
        self.__balance += balance

    def getbalance(self):
        return self.__balance

a1 = Account('Bhargavi',21)
print(a1.getbalance())
a1.display_balance(100)
print(a1.getbalance())