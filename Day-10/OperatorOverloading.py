class Employee:
    def __init__(self,salary,pf):
     self.salary=salary
     self.pf=pf

    def __add__(self,other): #e1-self, e2-other
     return self.salary+self.pf+other.salary+other.pf

    def __eq__(self,other): #overriding the function of ==
     if(self.pf==other.pf):
      return True
     else:
      return False



e1=Employee(1000,1500)
e2=Employee(1000,2000)
print(e1+e2)
print(e1==e2)


class TimeSheet:
    def __init__(self,name,days):
     self.name=name
     self.days=days

    def __mul__(self,other):
     return self.days*other.salary
    

ts=TimeSheet("siva",25)
print(ts*e1)
