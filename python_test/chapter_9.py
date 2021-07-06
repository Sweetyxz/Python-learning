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