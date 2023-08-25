import pandas as pd

x=[1,5,4,3,2]
y=pd.Series(x)
print(y)
print(y[4])

x1=[1,2,3,4,5,6,"end"]
y1=pd.Series(x1,index=["a","b","c","d","e","f","last"])
print(y1)

calories={
    "banana":89,
    "carrot":41,
    "beetroot":43
}

z=pd.Series(calories)
print(z)
z=pd.Series(calories,index=["carrot"])
print(z)