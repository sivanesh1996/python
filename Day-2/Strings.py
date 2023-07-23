x="""hi.iam hp
iam from america.
i have laptops,printers etc """

print(x)
print(type(x))

y="zia"
print(y[1])
print("length of y is: ",len(y))

z="kannada"
for z1 in z:
    print(z1)

a="apple is a fruit"
print("is" in a)

if "fruit" in a:
    print("it is present")

print("fruit" not in a)

if "banana" not in a:
    print("banana is not present")

#SLICING
  #0123456789 
i="jackieee c"
print(i[1:6])
print(len(i))

#last index is excluded

print(i[:2]) #prints from zero th index
print(i[9:]) #slice upto the end
  # 0   1   2   3   4   5
j=["k","i","l","l","e","r"]
  # -6  -5  -4  -3  -2  -1

print(j[1:-1])

#last index is excluded. if needed last index print(j[-4:])

k="Kssatta ice cream"
print(k.upper())
print(len(k))
print(k.lower())

l="  hp is a laptop company   "
print(l)
print(l.strip())

#replace()
m="mango is is a fruit"
print(m.replace("an","e"))

#split()
n="Hi, Siva"
print(n.split(","))

#concatenate
o="orange"
p="pulses"
print(o+p)
