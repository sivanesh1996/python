import numpy as np
from numpy import random

#random is an external module in numpy, so we must import additionally

#shuffle()

a=np.array([1,2,3,4,5])
random.shuffle(a)
print(a)

#given list is shuffled itself
a1=np.array([11,22,33,44,55])
random.permutation(a1) #given values not changed
print(a1)

b=random.permutation(a1)
print(b)
