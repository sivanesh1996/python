import datetime

x=datetime.datetime.now()
print(x)

print(x.year)
print(x.strftime("%A"))

#create datetime object

y=datetime.datetime(2017,10,17)
print(y)
print(y.strftime("%B"))
