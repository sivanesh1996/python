print(10>1)

a=11
b=12
if(a>b):
    print(a,"is greater")
else:
    print(b,"is greater")

#bool()
print(bool('hello')) #true
print(bool("")) #false
print(bool(None)) #false
print(bool(0)) #false
print(bool()) #false
print(bool(False)) #false
print(bool([])) #false
print(bool({})) #false

def myFunction():
    return True

print(myFunction())
if myFunction():
    print("Yes")
else:
    print("NO")

print(bool(0.222)) #true
print(bool([""])) #True 
#inside list empty string- True
print(bool(("")))  #False
#inside tuple empty string- False

a=None
print(id(a))
#output-9488912
b=None
print(id(b))
#output-9488912
