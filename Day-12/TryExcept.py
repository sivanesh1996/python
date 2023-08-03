try:
 print(x)
except:
 print("An exception occurred")


try:
 print(y)
except NameError:
 print("Variable x is not defined")
except:
 print("Something else went wrong")
finally:
 print("Iam finally block")

try:
 print("\nHello try block")
except:
 print("Exception occured")
else:
 print("No Error")

print("\nRaise an Exception")
'''
x=1
if x<=1:
 raise Exception("Number is less than or equal to 1")

age=17
if age<18:
 raise TypeError("age below 18 not allowed")

x=int(input('Enter x:'))
y=int(input('Enter y:'))
print(x/y) #y->0 Zero division error
'''
#print("muthu"+5) //Type Error
'''
try:
 x=int(input('Enter x:'))
 y=int(input('Enter y:'))
 print(x/y)
except (ZeroDivisionError,ValueError) as msg:
 print(msg)
 
 

file=open("/media/sivanesh/84567A75567A67B6/Python/Day-12/pincodes.txt")
#print(file.readline(),end='')

for each_line in file:
 print(each_line,end='')
file.close()


file=open("/media/sivanesh/84567A75567A67B6/Python/Day-12/pincodes.txt")
for each_line in file:
 (city,pincode)=each_line.split("-")
 print('pincode of',city,end='')
 print('is',pincode,end='')
file.close()


'''

def get_number():
 number=int(input("Enter PIN number"))
 return number

while True:
 try:
     print(get_number())
     option=input('Continue: Yes | No ')
     if option.lower() == 'no':
        break
 except ValueError:
        print("Please enter valid PIN no.")
