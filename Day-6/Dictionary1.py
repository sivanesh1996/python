mycar={
    "brand":"tata",
    "model":"indigo",
    "AC":True,
    "year":1996
}

mycar1=mycar

mycar["brake"]="drum"

print(mycar1)

mycar2=mycar.copy()
mycar["speed"]=150
print(mycar2)

mycar3=dict(mycar)
print(mycar3)

print("\nNested dictionaries")
myfamily={
    "child1":{
        "name":"emily",
        "year":2000
    },
    "child2":{
        "name":"toger",
        "year":2001
    },
    "child3":{
        "name":"linus",
        "year":2002
    }
}

print(myfamily)

mybike1={
    "model":"excel"
}
mybike2={
    "model":"splender"
}
mybike3={
    "model":"unicorn"
}

mybikes={
    "bike1":mybike1,
    "bike2":mybike2,
    "bike3":mybike3
}

print(mybikes)
print("\nACCESS NESTED")
print(myfamily["child2"]["name"])

print("\nfrom keys()")
x=('key1','key2','key3')
y=0

d1=dict.fromkeys(x,y)
print(d1)
d2=dict.fromkeys(x)
print(d2)

car={
    "brand":"maruti",
    "model":"dzire"
}

x=car.setdefault("speed","150")
print(x)

print(car)
