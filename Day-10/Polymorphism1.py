class Vehicle:
     def __init__(self,brand,model):
      self.brand=brand
      self.model=model
     def move(self):
      print("MOVE !")

class Car(Vehicle):
    pass

class Boat(Vehicle):
    
    def move(self):
     print("Sail !")

class Plane(Vehicle):
    def move(self):
     print("Fly !")

car1=Car("toyoto","innova")
boat1=Boat("Ibiza","Touring 1")
plane1=Plane("Boeing","747")

for x in (car1,boat1,plane1):
    print(x.brand)
    print(x.model)
    x.move()

'''
Car class is empty but it inherits the properties and methods from parent class.
Other classes also inherits the properites but overrides the move()
'''
