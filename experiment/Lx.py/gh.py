users = {
"user1": {"用户名": "user1", "密码": "123", "姓名": "后台管理员"},
"user2": {"用户名": "user2", "密码": "456", "姓名": "物流人员"},
"user3": {"用户名": "user3", "密码": "789", "姓名": "收银员"},
}

products = [
    {"编号":101, "名称": "薯片", "价格": 10},
    {"编号":102, "名称": "方便面", "价格": 12},
    {"编号":103, "名称": "吐司", "价格": 8},
]

def print_menu():
    print("------主菜单------")
    print("1. 显示商品列表")
    print("2. 增加商品信息")
    print("3. 删除商品信息")
    print("4. 修改商品信息")
    print("5. 退出")

def login():
    cs = 3
    while True:
        name = input("请输入您的用户名: ")
        if name in users:
            password = input("请输入您的密码: ")
            if password == users[name]["密码"]:
                print("登录成功! 欢迎你", users[name]["姓名"])
                cs = 3
                while True:
                    print_menu()
                    bh = input("请输入业务编号: ")
                    if bh == '1':
                        showproducts()
                    if bh == '2':
                        add_product()
                    if bh == '3':
                        del_product()
                    if bh == '4':
                        setprice()
                    if bh == '5':
                        return print("----正在退出----")
            
            else:
                cs -= 1
                print(f"还剩{cs}次机会")
                if cs == 0:
                    print("尝试次数已用完，程序退出。")
                    return

def showproducts():
    print("---编号---名称---价格")
    for product in products:
        print(f"---{product['编号']}---{product['名称']}---{product['价格']}")

def add_product():
    new_products = { }
    new_products['编号'] = int(input("请输入您想添加的商品编号: "))
    new_products['名称'] = input("请输入您想添加的商品名称: ")
    new_products['价格'] = int(input("请输入您想添加的商品价格: "))
    products.append(new_products)
    print(f"添加{new_products['名称']}成功, 添加后的商品信息如下: ")
    showproducts()

def del_product():
    delete = int(input("请输入您想删除的商品编号: "))
    
    for product in products[:]:
        if product['编号'] == delete:
            products.remove(product)
            print(f"正在删除{product['名称']}")
            print("删除商品成功！")
            showproducts()

def setprice ( ):
    pr_id = int(input("请输入要修改价格的商品编号: "))
    for product in products:
        if product['编号'] == pr_id:
            new_price = float(input("请输入新的商品价格: "))
            product['价格'] = new_price
            print(f"价格已设置成功。目前{product['名称']}为{product['价格']}")
            showproducts()

login()