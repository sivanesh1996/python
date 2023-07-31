class Parent:
    def __init__(self):
     print("Parent Constructor")

class Child(Parent):
    pass

ch=Child()


class Parent1:
    def __init__(self):
     print("Parent1 Constructor")

class Child1(Parent1):
    def __init__(self):
     super().__init__()
     print("Child1 constructor")

ch1=Child1()
