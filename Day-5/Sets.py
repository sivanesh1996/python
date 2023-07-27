mySet={"apple","banana","cherry","apple",1,True,"1"}
print(mySet)

print(len(mySet))

print("CONSTRUCTOR")
a=set((1,2,3,4,5))
print(a)

for x in a:
    print(x)

if 1 in a:
    print("Present")

print(1 in a)

print("ADD")

a.add(6)
print(a)

print("Add an exisiting set")
b={7,8,9}
a.update(b)
print(a)

c=[10,11]
a.update(c)
print(a)
print(type(a))

print("After Remove method")
a.remove(11)

print("After discard method")
a.discard(12)
print(a)

'''
print("clear method")
a.clear()
print(a)


print("del keyword")
del a
print(a)
'''
print("using for loop")
for x in a:
 print(x)



