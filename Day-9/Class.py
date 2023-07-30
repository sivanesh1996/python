class MyClass:
    x=5

p1=MyClass()
print(p1.x)

class Person:
    def __init__(self,name,age):
     self.name=name
     self.age=age

    def __str__(self):
     return f"{self.name} and age: {self.age}"

    def my_method(self):
     print("My name is:"+self.name)

i1=Person("Siva",22)
i2=Person("Ram",24)

print(i1.name)
print(i1.age)
print(i1)
print(i2)
i2.my_method()

class Car:
    def __init__(myObj,brand):
     myObj.brand=brand

    def my_function1(selfabcd):
     print("Car brand is:"+selfabcd.brand)

c1=Car("innova")
c1.my_function1()
c1.brand="fortuner"
c1.my_function1()
del c1
#c1.my_function1()

class Bike:
    pass
