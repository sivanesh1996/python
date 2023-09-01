from numpy import random

# x= random.normal(loc=2,scale=4,size=(2,3))
# print(x)

import seaborn as sns
import matplotlib.pyplot as plt

#using normal distribution in seaborn
sns.distplot(random.normal(loc=2,scale=4,size=(2,3)),hist=True)
plt.show()

#binomial distribtion

# y=random.binomial(n=5,p=0.5,size=5)
# print('binomial distribution')
# print(y)

#using binomial distribution in seaborn
# sns.distplot(random.binomial(n=5,p=0.2,size=5),hist=True)
# plt.show()