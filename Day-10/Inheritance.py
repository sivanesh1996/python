class Person:
    def __init__(self,fname,lname):
     self.fname=fname
     self.lname=lname
    def prints(self):
     print(self.fname ,self.lname)
p1=Person("Siva","Kumar")
p1.prints()

#child class
'''
class Student(Person):
    pass
s1=Student("Gopal","Ratnam")
s1.prints()
'''

class Student1(Person):
    def __init__(self,fname,lname):
     Person.__init__(self,fname,lname)

s2=Student1("Seetha","Jothi")
s2.prints()

#Adding another variable
class Student2(Person):
    def __init__(self,fname,lname):
     super().__init__(fname,lname)
     self.yearPassing=1999

s3=Student2("Raj","S")
print(s3.yearPassing)

class Student3(Person):
    def __init__(self,fname,lname,year):
     super().__init__(fname,lname)
     self.yearOfPass=year


#Add-methods

    def welcome(self):
     print("Welcome",s4.fname,s4.lname,"of year",s4.yearOfPass)
s4=Student3("Raja","Kumari",1999)
print(s4.yearOfPass)
s4.welcome()
     
