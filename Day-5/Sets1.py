a={1,2,3}
b={4,5,6}

#a.update(b)
#print(a)

a=a.union(b)
print(a)

print('To keep common items in both sets')
c={1,2,3}
d={4,5,6,1}
c.intersection_update(d)
print(c)
print(d)

print("intersection method-common values")
e={1,2,3}
f={4,5,6,1,2}
g=e.intersection(f)
print(g)

print("keep the items that are not common in both sets")
h={"apple","banana","cherry"}
i={"apple","jackfruit"}
#h.symmetric_difference_update(i)
#print(h)

j=h.symmetric_difference(i)
print(j)

print('difference method')
k={100,200,300,400}
l={100,500}
m=k.difference(l)
print(m) #200,300,400

print("\n difference_update method")
n={201,202,203}
o={201,204,205}
n.difference_update(o)
print(n)

print("isdisjoint method")
p=n.isdisjoint(o)
print(p)

print("issubset method")
q={1,2,3,4,5}
r={1,2,3,4,5,6,7}
s=q.issubset(r)
print(s)

print("issuperset method")
t={1,2,3,5,6,7,8,9,4}
u={1,2,3,4,5,6}
v=t.issuperset(u)
print(v)


