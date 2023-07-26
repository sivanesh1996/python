mytuple=("car","bike","scooter")
print(mytuple)
print(mytuple[0])
print(len(mytuple))

a=("apple",)
print(type(a))


print("Using constructor")
b=tuple(("apple","banana","duck"))
print(b)

print(b[0:1])

if "apple" in b:
    print("apple is present")

print("tuple changing values")
c=("maruthi","benz","honda")
print(c)
d=list(c)
d.insert(0,"opel")
c=tuple(d)

print(c)

d=("fiat",)
c=c+d
print(c)

print("tuple remove values")
e=("eli","elephant","end")
print(e)
f=list(e)
f.pop(0)
e=tuple(f)
print(e)

print("UNPACKING")
(e1,e2)=e
print(e1)
print(e2)

g=[1,2,3,4,5,6]
(g1,*g2,g3,g4)=g
print(g1)
print(g2)
print(g3)
print(g4)

for x in g:
    print(x)

h=(100,200,300,400,500)
for x in range(len(h)):
    print(h[x])

print("\nUsing while loop")
i=0
while i<len(h):
    print(h[i])
    i+=1

print("\nConcatenation")
j=(600,700,800,900)
h=h+j
print(h)

print("\nMultiplying tuple")
k=h*2
print(k)

print(k.count(100))
print(k.index(100))
