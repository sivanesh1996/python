result=lambda no:no*no

print(result(4))

print("\nFInd big number")

big_no=lambda no1,no2:no1 if no1>no2 else no2

print(big_no(5,55))

print("\nDisplay numbers divided by 3")

def my_function(n):
    if n%3==0:
        return True
    else:
        return False

li=[1,2,3,4,5,66,7,9]
print(list(filter(my_function,li)))

print("\nAnonymous function inside another function")

def my_function(n):
    return lambda a:n*a

my_tripler=my_function(3)
my_doubler=my_function(2)

print("Tripling the number:",my_tripler(4))
print("Doubling the number:",my_doubler(5))
