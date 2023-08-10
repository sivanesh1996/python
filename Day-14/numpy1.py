import numpy

x=numpy.array([1,4,7,2,5])
print(x)

#tuple
y=numpy.array((5,10,15,20))
print(y)

#2d
z=numpy.array([[3,6,9],[12,15,18]])
print(z)

#3d
z1=numpy.array([[[11,12,13],[14,15,16],[17,18,19],[20,21,22],[23,24,25]]])
print(z1)
print(z1.ndim)

#higher-order
z2=numpy.array([11,22,33,44],ndmin=6)
print(z2)
print(z2.ndim)
