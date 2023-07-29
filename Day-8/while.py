#using break statement , we can stop the loop even when while condition is true

i=1
while i<6:
    print(i)
    if(i==3):
        break
    i+=1

#to stop a current-iteration, we can use continue statement


j=10
while j<17:
    j+=1
    if j==15:  #we are skipping when j is equal to 15
        continue
    print(j)

#print a message once loop fails
k=20
while k<22:
    print(k)
    k+=1
else:
    print("loop ends")
   
