import numpy as np

#search-array

a=np.array([1,2,1,3,4,1,2])
b=np.where(a == 2)
print(b)

print("\nSearch sorted method")

c=np.searchsorted(a,1)
print(c)

d=np.searchsorted(a,[1,2,3])
print(d)

print("\nSort")

print(np.sort(a))

a1=np.array(["Catherine","Deepan","Abinaya","Raju","Bala"])
print(np.sort(a1))

a2=np.array([[6,5,7],[2,0,1]])
print(np.sort(a2))


print("\nFilter")
d1=np.array([1,2,3,4,5])
d2=[True,False,True,True,True]
e=d1[d2]
print(e)

f=np.array([50,60,71,80,76,88])
g=[]
for x in f:
    if x>70:
        g.append(True)
    else:
        g.append(False)
print(g)
h=f[g]
print(h)

print("\nShort form of above ")
i=f>70
j=f[i]
print(j)
