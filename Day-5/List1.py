#extract from lost based on certain condition: if list values contains letter 'a'
fruits=["apple","asparagus","litchie","mangostheen"]
newlist=[]

for x in fruits:
    if "a" in x:
        newlist.append(x)

print(newlist)

#by using list comprehension

print("LIST1")

list1=[x for x in fruits if "a" in x]
print(list1)

#to extract except "apple"
print("LIST-2")

list2=[x for x in fruits if x!="apple"]
print(list2)

#without if
print("LIST-3 ")

list3=[x for x in fruits]
print(list3)

#iterable
print("LIST-4")
list4=[x for x in range(len(list3))]
print(list4)

#print only even numbers
print("LIST-5")
list5=[x for x in range(10) if x%2==0]
print(list5)

#upper case and print
print("LIST-6")
list6=[x.upper() for x in fruits]
print(list6)

#expression can also contains conditions
#short form of if-else
print("LIST-7")
list7=[x if x!= "asparagus" else "amla" for x in fruits]
print(list7)

