fruits=["apple","cherry","cap","cat"]
for x in fruits:
    print(x)
    if x=="cap":
        break
else:
    print("loop ends") #else statement wont work if loop ends by break

#loop through string
for x in "banana":
    print(x)

#continue
nos=[1,2,3,4,5]
for x in nos:
    if x==4:
        continue
    print(x)

#range
print("\nRange")
for x in range(2,6):
    print(x)

#increment
print("\nIncrement the sequence by 2")
for x in range(0,7,2):
    print(x)

#inner loop
print("\nInner loop")
no1=[1,2,3,4,5]
no2=[11,22]
for x in no1:
    for y in no2:
        print(x,y)

print("\nPass statement")
for x in "apple":
    pass
