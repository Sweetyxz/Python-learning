#8-1 8-2 
'''
def display_message():
	print("i learn the def")
display_message()

def favorite_book(title):
	print(f"one of my favorite book is {title.title()}")
favorite_book('harry potter')
'''

'''
def name_book(name, book):
	print(f"{name} like {book}")
name_book(name = 'zyx', book = 'harry potter')
'''

'''
def name_book(name = 'zyx', book = 'hp'): #默认值
	print(f"{name} like {book}")
name_book()
'''

# 8-3 8-4 8-5
'''
def make_shirt(size, patten):
	print(f"the size is {size},the patten is {patten} ")
make_shirt('M', 'I LOVE CHINA')
make_shirt(patten = 'i LOVE my country', size = 'L')
'''

'''
def make_shirt(size, patten = 'i love python'):
	print(f"the size is {size},the patten is {patten} ")
make_shirt('m')
make_shirt('L')
make_shirt('s', 'i love php')

def describe_city(city, country = 'china'):
	print(f"{city} is in {country}")
describe_city('beijing')
describe_city('zhengzhou')
describe_city('new york', 'Amarica')
'''

#8-6  8-7 8-8
'''
def city_country(city, country):
	mes = f"{city}, {country}"
	return mes
message = city_country("beijing", "china")
print(message)
message = city_country("zhengzhou", "china")
print(message)
message = city_country("hangzhou", "china")
print(message)

def make_album(singer, album_name, num = None):
	album = {'singer': singer, 'album_name': album_name}
	if num:
		album['num'] = num
	return album
zyx = make_album('zyx', 'hi')
lmy = make_album('lmy', 'hello', num = 3)
print(zyx)
print(lmy)
'''

'''
def make_album(singer, album_name, num = None):
	album = {'singer': singer, 'album_name': album_name}
	if num:
		album['num'] = num
	return album
while True:
	print("press q to quit")
	name = input("name:")
	album_name = input("album_name:")
	if name == 'q' or album_name == 'q':
		break
	print(make_album(name, album_name))
'''

# 8-9 8-10 8-11
'''
mes = ["hi", "hello", "hh"]
sent_messages = []
def show_message(mes):
	for m in mes:
		print(m)

def send_messages(mes):
	while mes:
		x = mes.pop()
		sent_messages.append(x)

#sent_messages(mes) 原列表
send_messages(mes[:]) #副本
print(mes)
show_message(sent_messages)
'''

'''
def names(have_couple, *name): #传递任意数量的形参
	print(f"do they have couple? {have_couple}")
	for n in name:
		print(n)
names('yes', 'zyx', 'lmy', 'snn')
names('no', 'bo')

def name_location(name, age, **info): # 字典形参
	info['name'] = name
	info['age'] = age
	print(info)
name_location("zyx", '22', city = 'beijing', country = 'china')
'''

# 8-12 8-13 8-14
'''
def order(*fruit):
	print(f"you want {fruit} ")

order("banana")
order("apple", "orange", "milk")

def name_location(name, age, **info): # 字典形参
	info['name'] = name
	info['age'] = age
	print(info)
name_location("zyx", '22', city = 'beijing', country = 'china')

def car(make, version, **info):
	info['make'] = make
	info['version'] = version
	return info

cars = car('subaru', 'outback', color = 'blue', tow_package = 'True')
print(cars)
'''


