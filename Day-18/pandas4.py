import pandas as pd

df=pd.read_csv("/media/sivanesh/84567A75567A67B6/Python/Day-18/data.csv") #prints only first few and last few
#print(df)
#print(type(df))
#print(df.to_string())
#print(type(df.to_string()))

j= pd.read_json("/media/sivanesh/84567A75567A67B6/Python/Day-18/opendata.json")
print(j.to_string())