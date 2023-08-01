import mymodule as mx
import platform
from mymodule1 import greeting1

mx.greeting("Sivanesh")

a=mx.person["name"]
print(a)


print("\nBuilt-in Modules")
x=platform.system()
print(x)

y=dir(platform)
print(y)

greeting1("Rasathi")
