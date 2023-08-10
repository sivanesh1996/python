import numpy as np
#           0 1 2 3 4
a=np.array([1,2,3,4,5])
print(a[0:5])

b=np.array([0,1,2,3,4,5,6,7,8,9,10])
print(b[0:10:2])
print(b[-11:])

print("\n2D Slicing")
c=np.array([[1,2,3],[4,5,6]])
print(c[1,0:3])
#to print 3,6

print(c[0:2,2])

#to print [2,3][5,6]
print(c[0:2,1:3])
