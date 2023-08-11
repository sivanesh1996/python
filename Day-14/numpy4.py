import numpy as np

x=np.array([1,2,3])
print(x.dtype)

#we can convert to another datatype

y=np.array([11,22,33],dtype="S")
print(y)

#memory allocation in byte- answer will be in bits
z=np.array([1,2],dtype="i1")
print(z.dtype)


#astype function- create a duplicate copy 
z1=np.array([1.2,5.66])
z2= z1.astype("i")
print(z2) #output- [1,5]

#can use boolean
z3=np.array([1,2,0,5])
z4=z3.astype(bool)
print(z4)

#can use copy() to take a copy
a=np.array([100,200,300])
a1=a.copy()
a[0]=101
print(a)
print(a1)

#view() -->memory will be pointing to the specific variable, so whereever we change,that specific variable also change
b=np.array([21,31,41,51,61])
b1=b.view()
b[0]=25
print(b)
print(b1)
