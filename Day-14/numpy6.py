import numpy as np

print("Iterating 1 D")
a=np.array([1,2,3,4])

for x in a:
    print(x)

print("\n2D list by list")
b=np.array([[11,22,33],[44,55,66]])

for y in b:
    print(y)

for y in b:
    for y1 in y:
        print(y1)


print("\3d using nditer()")
c=np.array([[[1,2],[3,4],[5,6]]])

for z in np.nditer(c):
    print(z)

for x1 in np.nditer(a,flags=["buffered"],op_dtypes=["S"]):
    print(x1)

#flags bufferres is: is memory not enough it will take from buffer memory, op_dtype ->change datatype

#ndenumerate() - prints like (r,c)value
c1=np.array([[1,2,3],[4,5,6]])
for k in np.ndenumerate(c1):
    print(k)
