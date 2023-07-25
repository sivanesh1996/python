a=6
print(a>5 and a>4) #true
print(a>5 or a>4) #true
print(not(a>5 or a>4)) #false


print('Identical Operators')
b=[5]
c=[5]
d=b
print(b is d) #true
print(b is c) #false
print(b is not d) #false

print('Sequence Operators')
e=["banana","apple"]
print("banana" in e) #true
print("lemon" not in e) #true
