# 3-1 3-2 3-3
'''
names = ["ZYX", "SNN", "XXF" ,"NN"]
for i in range(0, len(names)):
	#print(names[i].title())
	mess = f"再不说话退群吧, {names[2].title()}"
	print(mess)

go_style = ["bike", "bus", "car"]
print("i like " + go_style[0])
print("i don't like " + go_style[1])
print("i hope i can have a " + go_style[2])
'''

'''
# insert()方法
names = ["xxf", "zyx", "snn", "nn"]
names.insert(1, "lmy")
print(names)
# 删除元素
# del
del names[1]
print(names)
#pop()
last_name = names.pop()
print(last_name)
print(names)
# pop(index)
second_name = names.pop(1)
print(second_name)
print(names)
#remove()
names.remove('snn')
print(names)
'''

# 3-4 3-5 3-6 3-7 

guests = ["xxf", "zyx", "snn", "nn"]
print(guests)

print(guests[1] + " can't go to the party")
guests[1] = "lmy"
for i  in guests:
	invent_mess = f"welcome to my party {i}"
	print(invent_mess)

print("i found a bigger table")
guests.insert(0, "gouli")
guests.insert(3, "dingcong")
guests.append("yy")
for j  in guests:
	invent_mess = f"welcome to my party {j}"
	print(invent_mess)

guests_num = len(guests)
print("the guest number is " + str(guests_num))

print("I can only invite two people")
while len(guests) != 2 :
	cancel_guests = guests.pop(0)
	print("i am so sorry " + cancel_guests)
print(guests)
print("you can still come to my party " + guests[0])
print("you can still can come to my party " + guests[1])
del guests[0]
del guests[0]
print(guests)


'''
cars = ["bmw", "audi", "toyota", "subaru"]
#cars.sort()
#cars.sort(reverse = True)
#print(sorted(cars))
#print(sorted(cars, reverse = True))
cars.reverse()
print(cars)
'''

#3-8 3-10
'''
travel_places = ["changsha", "tokoy", "guangzhou", "xiamen", "chengdu"]
print(travel_places)
print(sorted(travel_places))
print(travel_places)
print(sorted(travel_places, reverse = True))
print(travel_places)
travel_places.reverse()
print(travel_places)
travel_places.reverse()
print(travel_places)
travel_places.sort()
print(travel_places)
travel_places.sort(reverse = True)
print(travel_places)
'''

