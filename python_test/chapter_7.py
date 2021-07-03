'''
mes = input("输入姓名")
print(mes)
'''

#7-1 7-2 7-3
'''
car = input("what car would you like?")
print(f"let me see if i can find you a {car}")
'''

'''
people_num = input("how many people will come: ")
if int(people_num) > 8:
	print("there is no empty table")
else:
	print("there is a table")
'''
'''
num = input("input num: ")
if int(num) % 10 == 0:
	print("yes")
else:
	print("no")
'''

#7-4 7-5 7-6和7-4 一样
'''
flag = 1
while flag == 1:
	msg = input("peiliao: ")
	if msg == "quit":
		flag = 0
	else:
		print(f"we will put {msg} in pizza")
'''

'''
while True:
	msg = int(input("age: "))
	if msg <= 3:
		print('free')
	elif 3 < msg <= 12:
		print('10 doller')
	else:
		print('15 doller')
	break
'''

#7-8 7-9 7-10
'''
sandwich_orders = ['1', '2', '3']
fininshed_orders = []
while sandwich_orders:
	i = 0 
	print(f"i made {sandwich_orders[0]} sandwich")
	fininshed_orders.append(sandwich_orders[0])
	del sandwich_orders[0]
print(sandwich_orders)
print(fininshed_orders)
'''

'''
sandwich_orders = ['1', '4', '2', '4', '3', '4']
print(sandwich_orders)
print('4 has sold out')
while '4' in sandwich_orders:
	sandwich_orders.remove('4')
print(sandwich_orders)
'''

name_place = {}
msg = '1'
while msg != '0':
	name = input("name: ")
	place = input("place: ")
	name_place[name] = place

	msg = input("if you want to quit, input 0: ")

for k, v in name_place.items():
	print(f"{k}: {v}")



