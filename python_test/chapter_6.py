'''
name_age = {'zyx': 22, 'lmy': 23}
print(name_age)
name_age['snn'] = 23 #新增键值对
name_age['xxf'] = 23
print(name_age) #删除键值对
del name_age['lmy']
print(name_age)

other_name = name_age.get('nn', 'no such name') #get 方法
print(other_name)
'''

# 6-1 6-2 6-3
'''
my = {"firstname": 'z', 'lastname': 'yx', "age": 22, 'city': 'hangzhou'}
print(my['firstname'])
print(my['lastname'])
print(my['age'])
print(my['city'])

name_num = {'zyx': 22, 'lmy': 23, 'nn': 3, 'snn': 5, 'xxf': 6}
snn_num = name_num['snn']
print(f"snn's favority is {snn_num}")

pyt = {'list': 1, 'dic': 3, 'int': 4, 'float': 5, 'double': 2}
print(f"list: {pyt['list']}\n")
'''

'''
my = {"firstname": 'z', 'lastname': 'yx', "age": 22, 'city': 'hangzhou', "num": 22}
for key,value in my.items():# 遍历键值对
	print(f"key is {key}")
	print(f"value is {value}")
for k in my.keys(): #只输出键
	print(f"key is {k}")
for k in sorted(my.keys()): #排序后的键
	print(f"key is {k}")
for v in my.values(): #只输出键
	print(f"value is {v}")
for v in set(my.values()): #只输出键
	print(f"value is {v}")

my = {1, 2, 3, 2} #集合
print(my)
'''

#6-4 6-5 6-6
pyt = {'list': 1, 'dic': 3, 'int': 4, 'float': 5, 'double': 2}
for s, v in pyt.items():
	print(f"{s}: {v}")

river = {'changjiang': 'china', 'huanghe': 'china', 'mudanjiang': 'china'}
for ri, pl in river.items():
	print(f"{ri} runs through {pl}")
for ri in river.keys():
	print(ri)
for pl in river.values():
	print(pl)

name_num = {'zyx': 22, 'lmy': 23, 'nn': 3, 'snn': 5, 'xxf': 6}
part_in = ['snn', 'dc', 'zyx']
for i in part_in:
	if i in name_num.keys():
		print(f"{i}, thanks")
	else:
		print(f"{i}, please com" )
'''

#6-7 6-8 6-9 6-10 6-11 6-12
'''
my = {"firstname": 'z', 'lastname': 'yx', "age": 22, 'city': 'hangzhou'}
snn =  {"firstname": 's', 'lastname': 'nn', "age": 23, 'city': 'wuhan'}
nn =  {"firstname": 'z', 'lastname': 'ln', "age": 21, 'city': 'zhengzhou'}
people = [my, snn, nn]
for name in people:
	for key, value in name.items():
		print(f"{key}: {value}")

dog = {'type': 'keji', 'owner': 'nn'}
cat = {'type': 'jiafei', 'owner': 'pp'}
pets = [dog, cat]
for pet in pets:
	for key, value in pet.items():
		print(f"{key}: {value}")
'''

favority_places = {'nn': ['wuhan', 'hangzhou', 'changsha'], 'zyx': ['changsha', 'zhengzhou'], 'snn': ['wuhan']}
for key, values in favority_places.items():
	print(f"{key}'s favority is ")
	for v in values:
		print(v)

name_num = {'zyx': [22, 1], 'lmy': [23, 3], 'nn': [3, 4], 'snn': [5, 7], 'xxf': [6, 9]}
for name, num in name_num.items():
	print(f"{name}'s favority is ")
	for n in num:
		print(n)

cities = {
'hangzhou': {'country': 'china', 'pop': 23, 'face': 'beautiful'},
'wuhan': {'country': 'china', 'pop': 1, 'face': 'crowded'},
'beijing:': {'country': 'china', 'pop': 3, 'face': 'fanhua'}
}

for c, v in cities.items():
	print(f"this is {c}")
	for k, va in v.items():
		print(f"\t{k}: {va}")
