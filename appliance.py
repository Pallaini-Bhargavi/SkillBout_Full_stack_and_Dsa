from abc import ABC, abstractmethod
class Appliance(ABC):
    @abstractmethod
    def turn_on(self,pos):
        pass
    def turn_off(self,pos):
        pass

class Fridge(Appliance):
    def turn_on(self,pos):
        print(f"Fridge is {pos} now.")
    def turn_off(self,pos):
        print(f"Fridge is {pos} now")

class WashingMachine(Appliance):
    def turn_on(self,pos):
        print(f"Washing Machine is {pos} now.")
    def turn_off(self,pos):
        print(f"Washing Machine is {pos} now.")

f = Fridge()
w = WashingMachine()
f.turn_on("on")
f.turn_off("off")
w.turn_on("on")
w.turn_off("off")