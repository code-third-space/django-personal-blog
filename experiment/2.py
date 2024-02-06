'''
def g_f_n(f_n, l_n):
    full_name = f"{f_n} {l_n}"
    print(full_name)
man = g_f_n("jefs", "fefs")
print(man)

squares = [value**2 for value in range(1, 11)]
print(squares)

names = ['admin', 'Jaden', 'Emma', 'John', 'Sophia']
for name in names:
    if name == 'admin':
        print('Hello admin, would you like to see a status report?')
    else:
        print(f'Hello {name}, thank you for logging in again.')
'''
""" man = {
    'f_name': 'su',
    'l_name': 'luo',
    'age': '224',
    'city': 'cheng du',
}

count = 0  # 计数器

for ren in man:
    count += 1
    print(man[ren], end='')
    
    if count == 2:
        print()  # 在第二个值后换行 """

def make_sandwich(*ingredients):
    print("正在制作三明治，概述如下：")
    print("三明治的食材有：")
    for ingredient in ingredients:
        print("- " + ingredient)
    print("制作完成！\n")

# 调用函数三次，每次提供不同数量的实参
make_sandwich('火腿', '生菜', '番茄')
make_sandwich('鸡肉', '洋葱', '辣椒酱', '奶酪')
make_sandwich('鳄梨', '火鸡', '腌黄瓜')