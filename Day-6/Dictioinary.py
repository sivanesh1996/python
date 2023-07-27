mycar={
    "brand":"tata",
    "model":"indigo",
    "year":1996
}
print(mycar)

print("GET VALUES")
print(mycar["brand"])

print("CASE:DUPLICATE KEY")
car1={
    "brand":"toyoto",
    "model":"innova",
    "year":2011,
    "year":2020
}
print(car1)
print(len(car1))

car2={
    "brand":"toyoto",
    "model":"fortuner",
    "year":2011,
    "color":["red","white with blue sticker"],
    "year":2012
}
print(car2)

print("\nusing constructor")
car3=dict(name="john",country="usa",age=33)
print(car3)

print("\nGET METHOD")
print(car3.get("name"))
print(car3.get("names","wrong key"))
print(car3.keys())

print("\nAdd keys")
car3["color"]="white"
print(car3)
print("\nGET all values")
print(car3.values())

print("\nget every item as list")
list1=car3.items()
print(list1)

print("\nKey exists")
print("name" in car3)

print("\nChange value")
car2["year"]=2022
print(car2)

car2.update({"year":2023})
print(car2)

print("\nAdd new ")
car2["fuel"]="diesel"
print(car2)
car2.update({"AC":True})
print("\n",car2)

'''
print("\nRemove")
car2.pop("color")
print(car2)

del car2["year"]
print("\n",car2)

print("\nDelete entire dictionary")
del car2
print(car2)


car2.clear()
print(car2)
'''
print("\nLoop")
for x in car2:
    print(x) #prints keys

for x in car2:
    print(car2[x]) #print values

print("\nfor loop and values()")
for x in car2.values():
    print(x)

print("\nfor loop and keys()")
for x in car2.keys():
    print(x)

print("\nfor loop and items()")
for x,y in car2.items():
    print(x,y)


