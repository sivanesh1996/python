print("\nPrint numbers using Recusion")
def printNos(no):
    print(no)
    no+=1
    if no<=5:
       printNos(no)

printNos(1)

print("\nAddition of first 4 numbers using recursion")
def add(nos,total):
    total=total+nos
    nos=nos+1
    if nos<=4:
     return add(nos,total)
    else:
     return total


total=0
nos=1
print(add(nos,total))

print("\nMultiplication of first 4 numbers using Recursion. (Factorial)")
def factorial(n,fact):
    fact=fact*n
    n=n+1
    if n<=4:
     return factorial(n,fact)
    else:
     return fact

n=1
fact=1
print(factorial(n,fact))
