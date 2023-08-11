import numpy as np

a=np.array([[1,2,3],[4,5,6]])
print(a.shape)

#output-> (2,3) -->2->2 dimension 3->3 length

b=np.array([11,22,33,44,55],ndmin=5)
print(b.shape)
#output-(1, 1, 1, 1, 5) ->1 - no values in 1st 4 dimensions 5- 5 values in 5th dimension

c=np.array([1,2,3,4,5,6])
c1=c.reshape(2,3) #2->row 3->column
print(c1)

d=np.array([1,2,3,4,5,6,7,8,9,10,11,12])
d1=d.reshape(2,2,3) # 2 times 2 ->row 3-> column
print(d1)
d2=d.reshape(2,2,-1) #-1 -> auto calculate the column 
print(d2)

print(d1.base) #values before reshaping 

#multi-dimension to single dimension
e=np.array([[1,2,3],[4,5,6],[7,8,9]])
e1=e.reshape(-1)
print(e1)

