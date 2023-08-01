

print("\nLocal Scope")

def my_function():
    x=5
    print(x)
    def inside_function():
     print("inside function x incremented:",x+1)
    inside_function()

def my_function1():
    print(x) #trying to print x which is a local variable

my_function()
#my_function1()




print("\nGlobal Variable")
a="Hi.Iam Global variable"

def my_function2():
    print(a)
    global b
    b="iam global variable created inside local scope"

my_function2()
print("printing outside function:",b)

def my_function3():
    global a
    a="global variable edited"

my_function3()
print(a)


print("\nNaming variables")
c=500
def my_function4():
    c=300
    print(c)

my_function4()
print(c)


