price=49
txt= "The price of hero pen is {}"
print(txt.format(price))

txt1="The price is {:.2f}"
print(txt1.format(price))

quantity=5
itemno=292
price=99

myorder="I want {} pieces of itemno {} for {:.2f} dollars"
print(myorder.format(quantity,itemno,price))

speed=200
gear=6

car="My car is going in gear {1} with speed of {0} kmph and gear {1} got damaged"
print(car.format(speed,gear))

#named indexes

birthday="{name} birthday is on the month of {month} and {name} is waiting for her birthday"
print(birthday.format(name="Sheela",month="July"))
