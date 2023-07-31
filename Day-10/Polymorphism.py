class Car:
    def __init__(self,brand,model):
     self.brand=brand
     self.model=model
    def move(self):
     print("DRIVE !")

class Boat:
    def __init__(self,brand,model):
     self.brand=brand
     self.brand=brand
    def move(self):
     print("Sail !")

class Plane:
    def __init__(self,brand,model):
     self.brand=brand
     self.model=model
    def move(self):
     print("Fly !")

car1=Car("toyoto","innova")
boat1=Boat("Ibiza","Touring 1")
plane1=Plane("Boeing","747")

for x in (car1,boat1,plane1):
    x.move()
