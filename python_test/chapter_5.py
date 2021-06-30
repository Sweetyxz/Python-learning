# 5-1 5-2
'''
name = "Zyx"
print("is name == Zyx ? i think so")
print(name == "Zyx")
print("is name == lmy ? i think not")
print(name == "lmy")
print(name.lower() == "zyx")
'''

# 5-3 5-4 5-5 5-6 5-7
'''
alien_color = 'red'
if(alien_color == 'green'):
	print("you got 5 point")
elif (alien_color == 'yellow'):
	print("you got 10 point")
else:
	print("you got 15 point")

age = 65
if(age < 2):
	print("this is a baby")
elif(2 <= age < 4):
	print("this is a honey")
elif(4 <= age < 13):
	print("this is a child")
elif(13 <= age < 20):
	print("this is a teen")
elif(age >= 20):
	print("this is a man")

favorite_fruits = ["apple", "banana", "orange"]
if "apple" in favorite_fruits:
	print("you really love apple")
'''

'''
num = []
if num:
	print("yes")
else:
	print("no")
'''

# 5-8 5-9 5-10 5-11
people = ["zyx", "snn", "admin", "nn", "xxf"]
if people:
	for person in people:
		if(person == "admin"):
			print("hello admin")
		else:
			print(f"hi, {person}")
else:
	print("we need some users")


