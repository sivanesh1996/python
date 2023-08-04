import os
'''
f= open("//media//sivanesh//84567A75567A67B6//Python//Day-13//1.txt","w")

print("File Name is :",f.name)
print("File Mode is:",f.mode)
print("File Property", f.readable())
print("File Property", f.writable())
print("File is closed or not ",f.closed)
f.close()

print("File is closed or not ",f.closed)
'''

#f= open("//media//sivanesh//84567A75567A67B6//Python//Day-13//1.txt","r")

'''
f.write("I like apple juice\n") 
f.write("and jack fruit juice\n")
f.write("also strawberry juice")
list=["kamal\n","jenisha\n","rasathy\n","saravana\n"]
f.writelines(list)
f.close()
'''

#output=f.readline()
#output=f.readlines()
#info=" ".join(output)
#print(info)
#print(output)
#f.close()

#with statement
'''
with open("//media//sivanesh//84567A75567A67B6//Python//Day-13//1.txt","r") as f:
    output=f.readlines()
    info=" ".join(output)
    print(info)
'''

f= open("//media//sivanesh//84567A75567A67B6//Python//Day-13//1.txt","r")
print(f.tell())
output=f.readline()
print(f.tell())
f.seek(25)
print(f.tell())
info="-".join(output)
print(info) #I- -l-i-k-e- -a-p-p-l-e- -j-u-i-c-e-

if os.path.isfile("//media//sivanesh//84567A75567A67B6//Python//Day-13//1.txt"):
    print("File present")
f.close()

f1=open("/media/sivanesh/84567A75567A67B6/pic/rock.jpg","rb")
f2=open("/media/sivanesh/84567A75567A67B6/pic/rock1.jpg","wb")
data=f1.read()
#print(data)
f2.write(data)
f1.close()
f2.close()

#delete file

os.remove("/media/sivanesh/84567A75567A67B6/pic/rock1.jpg")
#os.rmdir("/media/sivanesh/84567A75567A67B6/pic/test")


