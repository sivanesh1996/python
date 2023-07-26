print("SORT ALPHABETICALLY")
fruits=["banana","strawberry","cranberry","apple","kiwi"]
print(fruits)
fruits.sort()
print(fruits)

print("sort numbers ascedning")
nos=[5,6,8,2,4,0,5,6,8]
print(nos)
nos.sort()
print(nos)

print("Number sort descending")
nos.sort(reverse=True)
print(nos)
fruits.sort(reverse=True)
print(fruits)

print("CASE IN-SENSITIVE SORT")
fr=["Orange","Banana","strawberry","apple"]
#fr.sort()
#print(fr)
fr.sort(key= str.lower)
print(fr)

print("REVERSE ORDER")
n=[1,2,3,4,5,6,7]
n.reverse()
print(n)

print("\nCOPY LIST")
veg=["keerai","vendaikai","brinjal"]
print(veg)
veg1=veg
veg.append("carrot")
print(veg1)

print("using copy()")
car=["maruti","bmw","benz"]
print(car)
car1=car.copy()
car.append("tata")
print(car1)

print("using list(args)-same as copy()")
lap=["hp","dell","sony","asus"]
print(lap)
lap1=list(lap)
lap.append("mac")
print(lap1)

print("JOIN 2 LISTS")
list1=["a","b","c","d"]
list2=[1,2]
list3=list1+list2;
print(list3)

print("\nAPPEND ONE LIST TO ANOTHER")
list4=["a","b"]
list5=[1,2]
for x in list4:
    list5.append(x)
print(list5)

print("\nAPPEND USING extend()")
list6=[1,2]
list4.extend(list6)
print(list4)
