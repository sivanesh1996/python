import pandas as pd
data = {
    "cars":["bmw","audi","tata","kia"],
    "rank":[5,4,3,2]
}

x=pd.DataFrame(data)
print(x)
print(type(x))
print(pd.__version__)