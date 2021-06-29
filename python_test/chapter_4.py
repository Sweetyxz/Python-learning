# 4-1 4-2 
'''
pizzas = ["bishengke", "sakezi", "yujianpisa", "join's pizza"]
for pizza in pizzas:
	print(pizza)
	print(f"i like {pizza}")
print("i really like pizza")

animals = ["fish", "cat", "dog", "pig"]
for animal in animals:
	print(animal)
	print(f"a {animal} would make a great pet")
print("any of these animals would make a great pet")
'''

'''
nums = list(range(0,10))
print(nums)

numss = list(range(0, 10, 2))
print(numss)

print(sum(nums))

squ = [value ** 2 for value in range(0, 3)]
print(squ)
'''

# 4-3 4-4 4-5 4-6 4-7 4-8 4-9
'''
for i in range(1, 21):
	print(i)
'''

'''
nums = [i for i in range(1,10001)]
print(max(nums))
print(min(nums))
print(sum(nums))
'''

'''
jinums = [i for i in range(1, 20, 2)]
for jinum in jinums:
	print(jinum)
'''

'''
nums3 = [i for i in range(3, 31, 3)]
for num3 in nums3:
	print(num3)
'''

'''
squli = [value ** 3 for value in range(1, 11)]
print(squli)
'''

'''
names = ["zyx", "xxf", "snn", "nn"]
print(names[0:3])
print(names[:3])
print(names[2:])
print(names[-3:])
print(names[0:4:3])

other_names = names[:] #复制列表使用切片 而非赋值
other_names.append("lmy")
print(other_names)
print(names)
'''

#4-10 4-11 4-12 4-12类似4-11
'''
names = ["zyx", "xxf", "snn", "nn"]
print("first three is " + " ".join(names[0:4]))
print("middle two is " + " ".join(names[1:3]))
print("last three is " + " ".join(names[-3:]))

pizzas = ["bishengke", "sakezi", "yujianpisa", "join's pizza"]
friend_pizzas = pizzas[:]
pizzas.append("mypizza")
friend_pizzas.append("herpizza")
for i in pizzas:
	print(f"my fav pizza are {i}" )
for j in friend_pizzas:
	print(f"my friends fav pizza are {j}" )
'''

'''
turp = (1,3)
print(turp[0])
print(turp[1])

turp = (1,)
print(turp[0])

turp = (2,5)
print(turp[0])
print(turp[1])
'''
# 4-13

foods = ("rice", "noodle", "fish", "meat", "frute")
for food in foods:
	print("before:" + food)
#foods[0] = "chicken"  python会报错

foods = ("chicken", "hot-pot", "fish", "meat", "frute")
for food in foods:
	print("after:" + food)

