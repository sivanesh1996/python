from numpy import random
import seaborn as se
import matplotlib.pyplot as plt

a= random.multinomial(n=6,pvals=[1/6,1/6,1/6,1/6,1/6,1/6,1/6])
print(a)