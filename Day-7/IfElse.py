a=2
b=5
if b>a:
    print("b is greater")
elif a>b:
    print("a is greater")
else:
    print("may be equal")

#short_hand_if

if b>a: print("b is greater")

#short_hand_if_else

print("a is not greater") if b>a else print("a is greaeter")

#multiple_if_else
print("Multiple if else")
c=20
d=20
print("c") if c>d else print("=") if c==d else print("d")

print("\nlogical operator")
e=3
f=4
g=5
if g>e and g>f:
    print("g is greater")

print("\nNOT keyword")
if not g<e:
    print("not keyword executed")

print("\nNESTED IF")
if g==5:
    print("inside if")
    if g<e:
        print("inside nested if")
    else:
        print("inside nested else")

print("\nPass statement")
if g==5:
    pass
