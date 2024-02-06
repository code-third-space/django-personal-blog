'''
str1 = "di {} si ren kou pu ca  jie guo xian shi, quan guo ren kou gong {} wan ren "
print(str1.format("7", "141178"))
'''
'''
str2 = "di {2} ci ren kou pu ca jie guo wei: quan guo ren kou gong {0} wan ren ,ping jun zeng zhang lv wei{1}%.".format(141178, 0.53, "qi")
print(str2)
'''
'''
student1 = ["liu yi", 18, "chong qing", '男']
print(student1[1])
'''
'''
import random #随机生成整数
li = [ ] #创建一个列表
for i in range(0, 100): #建立一个循环100次
    x = random.randint(70, 100) #随机生成
    li.append(x) #将x添加进li
    print(li[i], end = " ") #打印li, 并且不换行
    if (i + 1) % 10 == 0: #当i+1能被10整除
        print() #换行
maxnum  = max(li) #取li列表最大的元素
print(maxnum) #打印最大的数
print(li.index(maxnum)) #最大元素第一次出现的位置
print(li.count(maxnum)) #最大元素出现了多少次。
'''
'''
import random
s = [ ] #创建s列表
for i in range(1, 100): #建立循环,范围是1··100
    x = random.randint(97, 122) #随机生成26个数字
    if chr(x) not in s: #判断条件
        s.append(chr(x)) #将数字元素转换成26个字母
        if len(s) == 26: #判断条件
            break
s.sort(reverse = True) #逆向
print(s) #打印
'''
'''
li = [86, 72, 93, 90, 71, 56, 85, 88, 70, 95] #列表
s = 0 
n = 0
for i in li: #建立循环
    s += i 
ave = s / len(li) #取平均数
for i in li: #建立循环
    if i > ave: #判断条件
        n = n + 1 
print("ping jun shu wei{}, da yu ping jun shu de shu you {} ge.".format(ave, n)) #格式化
'''
'''
s = [8, 10, 2, 16, 14, 4, 6, 18, 12]
s.sort() #使用sort函数排序
print(s) 
x = 15
ps = len(s) #使用len函数
for i in s:
    if i > x:
        ps = s.index(i) #ps = i 》 x时i在s列表中的位置。
        break
s.insert(ps, x) #插入
print(s)
s.remove(10) # 删除
print(s)
'''
'''
a = [1, 2, 3, 4, 5]
print("初始列表位：", a)
x = a[-1]
a.pop(-1)
a.insert(0, x)
print("右移后的列表为： {}".format(a))
'''
'''
Dcountry = {"中国": "北京", "俄罗斯": "莫斯科", "法国": "巴黎"}
for key in Dcountry:
    print(key)
'''
'''
st = {'name': 'liuyi', 'age': '18', 'sex': 'man'}
st['age'] = 20
print(st)
'''
'''
st = {'name': 'liuyi', 'age': '18', 'sex': 'man'}
st['address'] = 'chongqiong'
print(st)
'''
'''
def g_f_n(f_n, l_n):  #创建一个函数
    full_name = f"{f_n} {l_n}" #创建了一个变量,将f_n和l_n组合在一起。
    return full_name.title() #将首字母大写。并返回给man
man = g_f_n("jimi", "hendrix") #man被赋值
print(man)
'''
'''
def get_f_n(f_n, l_n):
    full_name = f"{f_n} {l_n}"
    return full_name.title()
while True:
    print("\nPlease tell me your name:")
    f_name = input('first name: ')
    l_name = input('last name: ')
    for_name = get_f_n(f_name)
'''
'''
l = [1, 3, 2]
for i in l:
    print(f"I like {i} pizza.")
print("I really love pizza!")
'''
'''
animals = [5, 7, 3]
for animal in animals:
    print("A ",animal, "would make a great pet.")
print("s")
'''
'''
l = (range(1,1000001)) 
for i in l:             
    print(i)
    print(i)
print(min(l))
print(max(l))
print(sum(l))
###
l = list(range(1,1000001))
for i in l:
    print(i)
print(min(l))
print(max(l))
print(sum(l))
'''
'''
l = list(range(1, 20, 3)) #错
for i in l:
    print(i)

l = list(range(1, 21, 2))
for i in l:
    print(i)
'''
'''
l = list(range(3, 31, 2)) #错
for i in l:
    print(i)

l = list(range(3, 31, 3))
for i in l:
    print(i)
'''
'''
l = [ ]
for q in range(1, 11):
    i = q ** 3
    l.append(i)
for s in l:
    print(s)
'''
'''
l = list(q ** 3 for q in range(1,11))
for j in l:
    print(j)
'''
'''
print("The first three items in the list are:")
p =['The', 'first', 'three', 'items', 'in', 'the', 'list', 'are:']
print(p[ : 3])
print("Three items from the middle of the list are:")
k = ["Three", 'items', 'from', 'the', 'middle', 'of', 'the', 'list', "are:"]
print(k[3 : 6])
'''
'''
f_food = ('apple', 'bread', 'rice', 'egg', 'milk')
for food in f_food:
    print(food)
f_food = ('apple', 'noodles', 'ham', 'egg', 'milk')
for food in f_food:
    print(food)
'''
'''
print('apple' != 'orange')
print('apple' == 'orange')

car = 'Audi'
print(car.lower() == 'audi')

print(23 and 45 <= 100)
print((23 or 45) >= 100)
'''
'''
f_food = ['apple', 'bread', 'egg', 'rice', 'milk']
print('milk' in f_food)
print('apple' not in f_food)
'''
'''
alien_colors = ["green", "red"]
if 'yellow' in alien_colors:
    print("points: 5")
if "green" in alien_colors:
    print('5')
'''
'''
alien_colors = ['green', 'yellow']
if 'red' in alien_colors:
    print(5)
else:
    print(10)
'''
'''
age = float(input())
if 2 > age:
    print('yin er')
elif 2 <= age < 4:
    print('you er')
elif 4 <= age < 13:
    print('er tong')
elif 13 <= age <18:
    print('shao nian')
elif 18 <= age <65:
    print('zhong qing nian')
else:
    print('lao nian ren')
'''
'''
names = ['admin', 'Jaden', 'Emma', 'John', 'Sophia']
if len(names) == 0:
    print('We need to find some users!')
else:
    for name in names:
        if name == 'admin':
            print('Hello admin, would you like to see a status report?')
        else:
            print(f'Hello {name}, thank you for logging in again.')
'''
'''
cur_names = ['admin', 'Jaden', 'Emma', 'John', 'Sophia']
new_names = ['john', 'sunny', 'cat123', 'admin', 'Jaden']
xnames = []
cu_names = [name.lower() for name in cur_names]
for n_name in new_names:
    if n_name.lower() in cu_names:
        print(f"请输入别的用户名：{n_name}")
    else:
        xnames.append(n_name)
if len(xnames) == 0:
    print("所有用户名不可用，请输入别的用户名： ")
else:
    print("部分用户名可用：", xnames)
'''
'''
snm = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in snm:
    print(i)
    if snm == 1:
        print('1st')
    elif snm == 2:
        print('2nd')
    elif snm == 3:
        print('3rd')
    elif snm == 4:
        print('4th')
    elif snm == 5:
        print('5th')
    elif snm == 6:
        print('6th')
    elif snm == 7:
        print('7th')
    elif snm == 8:
        print('8th')
    else:
        print('9th')
'''
'''
numbers = list(range(1, 10))
for number in numbers:
    if number == 1:
        print(f'{number}st')
    elif number == 2:
        print(f'{number}nd')
    elif number == 3:
        print(f'{number}rd')
    else:
        print(f'{number}th')
'''
'''
man = {
    'f_name': 'su',
    'l_name': 'luo',
    'age': '224',
    'city':'cheng du',
    }
count = 0 #计数器
for ren in man:
    count += 1

    if count <= 2:
        print(man[ren], end = '')
    else:
        print()
        print(man[ren])
'''
'''
friends = {'Ethan': 42,
    'Olivia': 18,
    'Liam': 75,
    'Ava': 63,
    'Noah': 29
    }
for friend in friends:
    print(friend, end = ':')
    print(friends[friend])
'''

""" rivers = {'Thames River':'England ',
    'Rhine River':'Switzerland, Germany, France, Netherlands',
    'Ganges River':'India, Bangladesh',
    'Yangtze River':'china',
    'Mississippi River':'United States',
    }
for river, countries in rivers.items():
    print(f'\nThe {river.upper()} runs though {countries.upper()}')
for name in rivers.keys():
    print(f'\n{name.upper()}')
for name in rivers.values():
    print(f'\n{name.upper()}') """

""" existing_names = ['John', 'Emily', 'Michael', 'Sophia', 'Daniel']
survey_dict = {
    'John':'已参加',
    'Emily':'已参加',
    'Michael':'已参加',
    'David':'已参加',
}
for name in existing_names:
    if name in survey_dict:
        print(f'感谢{name}参加调查！')
    else:
        print(f'邀请{name}参加调查。') """

""" pets = [
    {'类型':'小狗', '主人': '小明'},
    {'类型':'猫', '主人':'小红'},
    {'类型':'鱼', '主人':'小李'},
    {'类型':'兔子', '主人':'小花'},
]
for pet in pets:
    print(f"类型:{pet['类型']}")
    print(f"主人:{pet['主人']}")
    print() """

""" favorite_places = {
    '小明':['北京','上海','成都'],
    '小红':['巴黎','伦敦'],
    '小李':['东京','纽约','悉尼']
}
for person, places in favorite_places.items():
    print(f'{person}喜欢的地方:')
    for place in places:
        print(place)
    print() """

""" cities = {
    '北京': {
        'country': '中国',
        'population': '2154万',
        'fact': '北京是中国的首都和政治中心。'
    },
    '巴黎': {
        'country': '法国',
        'population': '214万',
        'fact': '巴黎是法国的首都和文化中心。'
    },
    '纽约': {
        'country': '美国',
        'population': '855万',
        'fact': '纽约是美国的金融中心和国际都市。'
    },
}

for city, info in cities.items():
    print(f'{city}的信息')
    print(f'所属国家:{info["country"]}')
    print(f'人口约数:{info["population"]}')
    print(f'一个事实:{info["fact"]}')
    print() """

""" car_type = input('您想租什么样的汽车' )
print(f'让我看看能否为您找到一辆{car_type}') """

""" food_people = int(input('请问用餐的人有几位： '))
if food_people > 8:
    print('没有空桌！')
else:
    print('有空桌。') """

""" snm = float(input('请你输入一个数字 '))
if snm % 10 == 0:
    print('这个数是10的倍数。')
else:
    print('这个数不是10的倍数。') """

""" prompt = ('请输入比萨配料(输入"quit"结束程序')
message = ''
while message != 'quit':
    message = input(prompt)
    if message != 'quit':
        print(f'将{message}添加到比萨中。') """

""" prompt = ("你的年龄： ")
age = ''
while age != 'quit':
    age = float(input(prompt))
    if age == 'quit':
        break
    if age < 3:
        print("免费！")
    elif 3 <= age < 12:
        print("10美元!")
    elif age >= 12:
        print("15美元!") """

""" prompt = ("你的年龄： ")
age = input(prompt)
while age != 'quit':
    age = float(age)
    if age < 3:
        print("免费！")
    elif 3 <= age < 12:
        print("10美元!")
    else:
        print("15美元!")
    age = input(prompt) """

""" prompt = ("你的年龄： ")
age = input(prompt)
active = True

while active:
    if age == 'quit':
        active = False
    else:
        age = float(age)
        if age < 3:
            print("免费！")
        elif 3 <= age < 12:
            print("10美元!")
        else:
            print("15美元!")
        age = input(prompt)  """

""" prompt = "你的年龄: "
age = ''
while True:
    age = input(prompt)
    if age == 'quit':
        break
    else:
        age = float(age)
        if age < 3:
            print("免费！")
        elif 3 <= age < 12:
            print("10美元!")
        else:
            print("15美元!") """

""" sandwich_orders = ['tuna sandwich', 'chicken sandwich', 'ham sandwich']
finished_sandwiches = [ ]

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print('I made your' + sandwich + '.')
    finished_sandwiches.append(sandwich)
print("Here are the finished sandwiches:")
for finished in finished_sandwiches:
    print(finished) """

""" sandwich_orders = ['tuna sandwich',
    'chicken sandwich',
    'ham sandwich',
    'pastrami',
    'pastrami',
    'pastrami',
    ]
finished_sandwiches = [ ]

print("很抱歉,熟食店的五香烟熏牛肉('pastrami')卖完了。")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
    print("熟食店的五香烟熏牛肉('pastrami')三明治无法制作。")
finished_sandwiches = sandwich_orders.copy()
      
for finished in finished_sandwiches:
    print(finished)
print("最终的列表 finished_sandwiches 中未包含 'pastrami'。") """#有问题

""" def display_message():
    print("本章的主题是函数和代码组织。")
display_message() """

""" def favorite_book(title):
    print(f"One of my favorite books is {title.capitalize()}")
favorite_book('three people') """

""" def city_country(city, country):
    return f'{city.title()}, {country.title()}'
print(city_country("beijing", "china"))
print(city_country("paris", "france"))
print(city_country("london", "united kingdom")) """

""" def show_messages(messages):
    for message in messages:
        print(message)
         
text_messages = ["Hello", "How are you?", "Welcome!", "Goodbye"]
show_messages(text_messages) """

""" def send_messages(messages):
    sent_messages = [ ]
    while messages:
        current_message = messages.pop(0)
        print(current_message)
        sent_messages.append(current_message)
    return sent_messages
    
text_messages = ["Hello", "How are you?", "Welcome!", "Goodbye"]

sent_messages = send_messages(text_messages[:])

print("original messages: ")
print(text_messages)
print("sent message: ")
print(sent_messages) """#？？？？？？？？？？

""" def make_sandwich(*ingredients):
    print("正在制作三明治，概述如下：")
    print("三明治的食材有：")
    for ingredient in ingredients:
        print("-" + ingredient)
    print("制作完成 \n")

make_sandwich('火腿', '生菜', '番茄')
make_sandwich('鸡肉', '洋葱', '辣椒酱', '奶酪')
make_sandwich('鳄梨', '火鸡', '腌黄瓜') """

""" def make_car(manufacturer, model, **car_info):
    car = {
        'manufacturer': manufacturer,
        'model': model
    }
    car.update(car_info)
    return car
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print("Car Information:")
for k, v in car.items():
    print(f"{k}, {v}") """