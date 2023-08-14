import numpy as np
#1-d concatenate

arr1=np.array([1,2,3])
arr2=np.array([4,5,6])
arr=np.concatenate((arr1,arr2))

print(arr)

#2-d concatenate

arr3=np.array([[1,2,3],[4,5,6]])
arr4=np.array([[7,7,7],[8,8,8]])
arr5=np.concatenate((arr3,arr4),axis=1)
print(arr5)

#stack create its axis

print("\n")

arr6=np.array([[1,2],[3,4]])
arr7=np.array([[5,6],[7,8]])
arr8=np.stack((arr6,arr7),axis=1)
print(arr8)

print("\nPrint rows")
arr8=np.hstack((arr6,arr7))
print(arr8)

print("\nPrint columns")
arr8=np.vstack((arr6,arr7))
print(arr8)

print("\nPrintng same height")
arr8=np.dstack((arr6,arr7))
print(arr8)

print("\nSplit")
arr10=np.array([1,2,3,4,5,6,7,8,9])
arr11=np.array_split(arr10,3)
print(arr11)
print(arr11[0])
