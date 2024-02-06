user1 = {"用户名": "user1", "密码": "123", "姓名": "后台管理员"}
user2 = {"用户名": "user2", "密码": "456", "姓名": "物流人员"}
user3 = {"用户名": "user3", "密码": "789", "姓名": "收银员"}
def login():
    while True:
        name = input("请输入您的用户名: ")
        if name == user1["用户名"]:
            password = input("请输入您的密码: ")
            if password == user1["密码"]:
                print("登录成功! 欢迎你", user1["姓名"])
login()