import sys

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
finally:
 print("Check finally")
 '''
 
'''
file=open("/media/sivanesh/84567A75567A67B6/Python/Day-12/pincodes.txt")
#print(file.readline(),end='')

for each_line in file:
 print(each_line,end='')
file.close()
'''
'''
try:
 file=open("/media/sivanesh/84567A75567A67B6/Python/Day-12/pincodes.txt")
 for each_line in file:
  try:
   (city,pincode)=each_line.split("-")
   print('pincode of',city,end='')
   print('is',pincode,end='')
  except ValueError:
   print('Check split')

 file.close()
except:
 print('please check file location')

'''


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
 except:
        print("Please check some other issues")

'''
print('\nHandling List')
inputList=['a',0,2,8,10,False]

for entry in inputList:
    try:
        print("The entry is",entry)
        r=1/int(entry)
        break
    except:
        print("Oops!",sys.exc_info() [1], "occurred")
        print("Next entry.")
        print()
print("The reciprocal of ",entry,"is",r)
