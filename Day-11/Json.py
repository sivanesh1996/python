import json

a='{"name":"John","age":22,"city":"nagercoil"}'

#converts json to dictionary
b=json.loads(a)

print(b)
print(b["name"])
print(type(b))

c={
    "brand":"maruti",
    "model":"dzire",
    "fuel":"petrol"
}
#converts from python to json
print("\nPython to dictionary")
d=json.dumps(c)
print(d)
print(type(d))


