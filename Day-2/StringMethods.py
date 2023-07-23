#capitalize- converts the first letter to capital

a="hi iam siavenesh.iam 28"
print(a.capitalize())

#casefold- string into lower case
b="BIBLe"
print(b.casefold())

#center
c="banana"
print(c.center(10))
print(c.center(10,"0"))

#count- returns the number of times ,the value appears in the string
c="banana"
print(c.count("a"))

print(c.count("a",0,2))

#endswith("str") endswith("str",index1,index2)
print(c.endswith("na"))

#find() -search and return the index-first occurance only
#find("str",index1,index2)
print(c.find("a"))

#format - insert a number in a placeholder
d="Rubber {price:.2f}"
print(d.format(price=2))

#index() - find method returns -1 if not found but index() if value is not found,it raises an exception
#index("str",index1,index2)
e="rubber"
print(e.index("b"))

#isalnum() - returns true if all characters are alpha numberic
f="aibaj1"
print(f.isalnum())

#isalpha() -returns true if all characters are only alphabets
g="11"
print(g.isalpha())

#isdecimal()
h="11"
print(h.isdecimal())

#isidentifier()
i="2Myvar"
print(i.isidentifier())

#islower()
j="hello"
print(j.islower())

#isspace() - returns true if the string have only whitespaces
k=" "
print(k.isspace())

#isupper() 
l="MNO"
print(l.isupper())

#join() - joins the element of an iterable to the end of string
myTuple=("siva","sundar","raj")
m="ooooo".join(myTuple)
print(m)

#lstrip -left strip
n="   banana  "
print(n.lstrip() +"is a fruit")

o="..,,jackychan"
print(o.lstrip(",."))


#partition - search specified string and splits the string into tuple containing 3 elements
p="hi iam siva from iam india"
print(p.partition("iam"))

#replace - all occurance of a specified word is replaced
q="hi hi hi kk"
print(q.replace("hi","ok"))

print(q.replace("hi","be",2)) #2 is the occurance

#rfind() - returns the last occurance of string. if not found,returns -1
#rfind("value",startIndex,endIndex)
r="sls"
print(r.rfind("s"))

#rindex() -same as rfind()-difference is that this method raises error if not found

#rjust() - right justification
s="apple"
t=s.rjust(20)
print(t+" is a fruit")
print(s.rjust(20,"7") +" is a healthy food")

#rpartition - partition() like but search from right to left
u="apple mango apple"
print(u.rpartition("apple"))

#rsplit -same as split but starts from right. it has max value
v="berries,almond,cashew,peanuts"
print(v.rsplit(","))
print(v.split(",",1))

#split
w="circle round rectangle"
print(w.split()) #default separator is whitespace
print(w.split(" ",1))

#splitlines- split based on new line \n
#string.splitlines(keeplinebreaks)  true-keep the line break, default is false
x="mouse\nkeyboard speaker"
print(x.splitlines())
print(x.splitlines(True))

#startswith
y="key"
print(y.startswith("k"))
z="jungle is forest"
print(z.startswith("f",10,12)) #index

#strip 
a1="  banana   "
print(a1.strip()+"is a fruit")
a2="oooooooobananaslllllllll"
print(a2.strip("ol"))

#swapcase() - uppercase becomes lower case and vice versa
b1="aLwIn"
print(b1.swapcase())

#title() -first letter of every word is capital, after number,first letter is capital
c1="Hi Welcome to 2b2b2b 2mkdk"
print(c1.title())

#translate() -use a dictionary with ascii codes to replace
mydict={65:66}
d1="AAAAAAQQAAA"
print(d1.translate(mydict))

#upper()
e1="siavnesH"
print(e1.upper())

#zfill() -  add zero's to the beginning of the string until it reaches specified length
f1="kl"
print(f1.zfill(3))

