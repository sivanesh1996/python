a=["mango","strawberry","cocunut"]
print(a)

print(len(a))

#using list constructor
#           -4       -3          -2         -1
b=list(("square","rectangle","triangle","sphere"))
print(b)

print(b[0])

print(b[0:4])
print(b[-4:-1])

#check
print(("square" in b))

c=["volvo","benz","scania","tata"]
print(c)
#changeable
c[0]="bmw"
print(c)
c[0:2]=["volvo","toyoto","maruti"]
print(c)

#replace
d=["dog","domer","keeri","browny"]
d[0:2]=["crocodile"]
print(d)
#insert
d.insert(0,"blacky")
print(d)

#append
d.append("tony")
print(d)

#extend
e=["elephant","emo kozhi","echer"]
f=["frog","freshness"]
e.extend(f)
print(e)

#extend with tuple
g=("giraffe","gulf")
e.extend(g)
print(e)

#remove specific item
h=["pencil","rubber","scale"]
h.remove("pencil")
print(h)

#remove specific index
i=["italy","iron","iridium","illuminator","iri"]
print(i)
i.pop(2)
print(i)
i.pop()
print(i)
del i[0]
print(i)

#delete entire list
#del i
#print(i)

#clear entire list
i.clear()
print(i)

#loop list
print("loop through list")
list1=["mango","sapotta","grape","orange"]
for x in list1:
    print(x)


print("using index in loop")
for x in range(len(list1)):
    print(list1[x])


print("using while loop")
i=0
while i<len(list1):
    print(list1[i])
    i+=1

print("Comprehensive list")
[print(x) for x in list1]

