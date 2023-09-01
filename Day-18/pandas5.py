import pandas as pd

x=pd.read_csv("/media/sivanesh/84567A75567A67B6/Python/Day-18/data.csv")
print(x.head(20))
print(x.tail(7))

print(x.info())