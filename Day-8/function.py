def my_function():
    print("Hello function")

my_function() #calling

#arguments

def my_function(fname,lname):
    print(fname+" "+lname)

my_function("Siva","Kumar")

#arbitary arguments
print("\n*Arbitary arguments")
def my_function1(*name):
    print(name[1])

my_function1("John","Sundar")


print("\nKeyword arguments")
def my_function2(child1,child2):
    print(child2)

my_function2(child2="bruce",child1="anand")

print("\n**kwargs")
def my_function3(**kids):
    print(kids["lname"])

my_function3(fname="sankar",lname="Lal")

print("\nDEfault parameter")
def my_function4(country="India"):
    print(country)

my_function4("Norway")
my_function4()

print("\nPassing list as args")
def my_function5(fruits):
    for x in fruits:
        print(x)

fruits=["apple","cherry","grape"]
my_function5(fruits)

print("\nReturn statement")
def my_function6(no):
    return no*6

print(my_function6(6))

print("\npass statement")
def my_function7():
    pass

my_function7()
