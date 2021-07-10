import json
'''
with open('pi_digits.txt') as file_object:
    #contents = file_object.read() 
    #print(contents.rstrip())
    #for f in file_object:
        #print(f.rstrip())
    lines = file_object.readlines()
for l in lines:
    print(l.rstrip())
'''

# 10-1 10-2
'''
with open('learn_python.txt') as f:
    #contents = f.read()
    #print(contents)
    #for i in f:
    #   print(i.rstrip())
    lines = f.readlines()
    print(lines)
    for i in lines:
        print(i.replace('python', 'java')) #replace()不会替换原来字符串的内容
'''

#10-3 10-4 10-5类似
'''
while True:
    print("please enter q to exit")
    name = input("please enter your name:")
    if name == 'q':
        break
    else:
        with open('name.txt', 'a') as f:
            f.write(name + ',thank you for coming\n')
'''
'''
try:
    print(5/0)
except ZeroDivisionError:
    print('no zero')
'''
'''
try:
    with open('a.txt') as f:
        contents = f.read()
except FileNotFoundError:
    print("we can not found the file")
else:
    print(contents)
'''

# 10-6 10-7 与前面的类似：10-8 10-9 10-10
'''
while True:
    print("enter q to exit")
    a = input("please enter the first num:")
    b = input("please enter the second num:")
    if a == 'q' or b == 'q':
        break
    else:
        try:
            num = int(a) + int(b)
        except ValueError:
            print("YOU SHOULD INPUT A NUMBER")
        else:
            print(num)
'''

# 10-11 10-12 10-13
'''
filename = 'num.jaon'
num = input("please enter your favorite num:")
with open(filename, 'w') as f:
    json.dump(num, f)
with open(filename) as f:
    number = json.load(f)
    print(f"i know your favorite number is {number}")
'''
filename = 'num.json'


def is_store_name():
    try:
        with open(filename) as f:
            number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return number


def no_store_name():
    num = input("please enter your favorite num:")
    with open(filename, 'w') as f:
        json.dump(num, f)


def greet_user():
    user = is_store_name()
    if user:
        print(f"hello {user}")
    else:
        no_store_name()


greet_user()
