from numpy import random
a=random.randint(100)
print(a)

b=random.rand()
print(b)

#print many random numbers
c=random.randint(100,size=4)
print(c)

#print random numbers in multi-dimension [r,c]
d=random.randint(100 , size=(2,5))
print(d)

#print 0-1 values in multi-dimension
e=random.rand(2,5)
print(e)

#print within a given list in random
f=random.choice([4,5,6,77,3,1])
print(f)

#print a specific size
g=random.choice([1,2,3,4,5,6],size=2)
print(g)

h=random.choice([9,8,7,6],size=(2,4))
print(h)

