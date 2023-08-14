from numpy import random
'''
p -> probabitiy - chances 
0-1
if added all, it should get 1
'''
a=random.choice([3,4,2,1],p=[0.1,0.3,0.2,0.4],size=9)
print(a)

b=random.choice([3,4,2,1],p=[0.1,0.3,0.2,0.4],size=(3,5))
print(b)
