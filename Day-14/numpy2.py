import numpy as np
#indexing

a=np.array(["Hello",2,"World"])
print(a[0],a[2])

#2d

b=np.array([[1,2,3],[4,5,6]])
print(b[1,2])

#3d

c=np.array([[[11,22],[33,44],[55,66]]])
print(c[0,2]) #prints [55,66]
print(c[0,2,1]) #prints 66
