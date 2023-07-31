mytuple=("apple","banana","lemon")
myit=iter(mytuple)

print(next(myit))
print(next(myit))
print(next(myit))

s="queen"
myit1=iter(s)

print(next(myit1))
print(next(myit1))
print(next(myit1))
print(next(myit1))
print(next(myit1))


print("\n__iter__() and __next__()")

class MyNumbers:
    def __iter__(self):
     self.a=1
     return self
    def __next__(self):
     val=self.a
     self.a+=2
     return val

values=MyNumbers()
myitr=values.__iter__()
print(myitr.__next__())
print(myitr.__next__())
print(myitr.__next__())

#the above print has no end

