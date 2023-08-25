import pandas as pd

a={
    "calories":[200,600],
    "time":[20,60]
}
b=pd.DataFrame(a,index=["day1","day2"])
print(b)
#print(b.loc[[1,0]])
print(b.loc["day2"])