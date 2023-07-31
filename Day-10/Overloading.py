#default arguments

def my_function(num=2,num1=4):
    print(num+num1)

my_function()
my_function(num1=5)
my_function(6)


#variable length arguments

def add(*no):
    total=0
    for i in no:
     total=total+i
    print(total)

add(1,2,3)
