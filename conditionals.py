#look at a temperature and figure out what state  water is in - solid, liquid or gas

# set the temperature first
temp = int(input("enter a temperature\n"))

if temp < 4:
	print("water is frozen - a solid")

elif temp > 4 and temp < 100:
	print("water is liqiud")

elif temp >= 100:
	print("water is a gas")

else:
	print("you didn't enter a number, try again")