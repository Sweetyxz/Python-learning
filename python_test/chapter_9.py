# 9-1 9-2 9-3
'''
class Restaurant:
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
	def  describe_restaurant(self):
		print(f"{self.restaurant_name} is {self.cuisine_type}")
	def open_restaurant(self):
		print("Restaurant is opening")

res = Restaurant('luomocun', 'chinese food')
res.describe_restaurant()
res.open_restaurant()

res1 = Restaurant('panggelia', 'rouxiebao')
res1.describe_restaurant()
res2 = Restaurant('haidilao', 'huoguo')
res2.describe_restaurant()
'''
'''
class User:
	"""docstring for ClassName"""
	def __init__(self, first_name, last_name, age):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
	def describe_user(self):
		print(f"{self.first_name} {self.last_name}, your age is {self.age}")
	def greet_user(self):
		print(f"hello, {self.last_name.title()}")

my = User('zhao', 'yx', 22)
my.describe_user()
my.greet_user()						
'''

# 9-4 9-5 
'''
class Restaurant:
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		self.number_served = 0
	def  describe_restaurant(self):
		print(f"{self.restaurant_name} is {self.cuisine_type}")
	def open_restaurant(self):
		print("Restaurant is opening")
	def eat_num(self):
		print(f"there are {self.number_served} people already eat")
	def set_number_served(self, num):
		self.number_served = num
	def increment_number_served(self, incre_num):
		self.number_served += incre_num

res = Restaurant('luomocun', 'chinese food')
res.describe_restaurant()
res.open_restaurant()
res.eat_num()
res.number_served = 5
res.eat_num()
res.set_number_served(10)
res.eat_num()
res.increment_number_served(20)
res.eat_num()
'''

'''
class User:
	"""docstring for ClassName"""
	def __init__(self, first_name, last_name, age):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
		self.login_attempts = 0
	def describe_user(self):
		print(f"{self.first_name} {self.last_name}, your age is {self.age}")
	def greet_user(self):
		print(f"hello, {self.last_name.title()}")
	def increment_login_attempts(self):
		self.login_attempts += 1
	def reset_login_attempts(self):
		self.login_attempts = 0
		

my = User('zhao', 'yx', 22)
my.describe_user()
my.greet_user()
for i in range(1, 10):
	my.increment_login_attempts()
	print(f"increment num: {my.login_attempts}")
my.reset_login_attempts()
print(f"reset num: {my.login_attempts}")
'''

#9-6 9-7 9-8 9-9
'''
class Restaurant:
	def __init__(self, restaurant_name, cuisine_type):
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
	def  describe_restaurant(self):
		print(f"{self.restaurant_name} is {self.cuisine_type}")
	def open_restaurant(self):
		print("Restaurant is opening")

class Icecreamstand(Restaurant):
	"""docstring for Icecreamstand"""
	def __init__(self, restaurant_name, cuisine_type, flavors):
		super().__init__(restaurant_name, cuisine_type)
		self.flavors = flavors
	def print_flavors(self):
		print(self.flavors)

ice = Icecreamstand('kaixin', 'tianpin', ['apple', 'orange', 'milk'])
ice.print_flavors()
'''
'''
class User:
	"""docstring for ClassName"""
	def __init__(self, first_name, last_name, age):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
	def describe_user(self):
		print(f"{self.first_name} {self.last_name}, your age is {self.age}")
	def greet_user(self):
		print(f"hello, {self.last_name.title()}")

class Admin(User):
	"""docstring for Admin"""
	def __init__(self, first_name, last_name, age, privileges):
		super().__init__(first_name, last_name, age)
		self.privileges = privileges
	def show_privileges(self):
		print("the admin powers are as follows:")
		for p in self.privileges:
			print(p)
ad = Admin('Z', 'yx', 22, ['can add post', 'can delete post'])
ad.show_privileges()
'''
'''
class User:
	"""docstring for ClassName"""
	def __init__(self, first_name, last_name, age):
		self.first_name = first_name
		self.last_name = last_name
		self.age = age
	def describe_user(self):
		print(f"{self.first_name} {self.last_name}, your age is {self.age}")
	def greet_user(self):
		print(f"hello, {self.last_name.title()}")

class privileges():
	def __init__(self, privileges):
		self.privileges = privileges
	def show_privileges(self):
		print("the admin powers are as follows:")
		for p in self.privileges:
			print(p)

class Admin(User):
	"""docstring for Admin"""
	def __init__(self, first_name, last_name, age, privileges):
		super().__init__(first_name, last_name, age)
		self.privileges = privileges

pr = privileges(['can add post', 'can delete post'])
ad = Admin('Z', 'yx', 22, pr)
ad.privileges.show_privileges()
'''
from random import randint
from random import choice
'''
x = randint(1, 6)
print(x)

name = ['zyx', 'snn', 'lmy']
n = choice(name)
print(n)
'''

# 9-13  9-14 9-15 9-16
'''
class Die:
	def __init__(self):
		self.sides = 6
	def roll_die(self):
		self.sides = randint(1, 6)
die = Die()
for i in range(1, 11):
	die.roll_die()
	print(f"the {i}th is {die.sides}")
'''

'''
lis = []
award = []
for i in range(1, 11):
	lis.append(str(randint(1,9)))
print(lis)
lis.append('a')
lis.append('b')
lis.append('c')
lis.append('d')
lis.append('e')
print(lis)

for j in range(1, 6):
	award.append(choice(lis))

print(f"if you num is {award}, you will win a award")
'''