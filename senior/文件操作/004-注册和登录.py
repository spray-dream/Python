# -*- coding = utf-8 -*-
# @Time : 2021/8/1 13:52
# @Author : spray_dream
# @File : 004-注册和登录.py
# @Software: PyCharm


def reader():
    global list1, list2, list3
    list1 = []
    list2 = []
    list3 = []
    with open('./user.txt', 'a+') as f1:
        f1.seek(0)
        content1 = f1.readlines()
        print("用户有:", content1)
        for i in content1:
            i = i.replace('\n', '')
            i = i.split(':')
            list1.append(i[0])
            list2.append(i[1])
    with open('lock.txt', 'a+', encoding='utf-8') as f2:
        f2.seek(0)
        content2 = f2.readlines()
        print("被锁定用户有:", content2)
        for i in content2:
            i = i.replace('\n', '')
            list3.append(i)

# 注册功能
def register():
    while True:
        username = input("欢迎, 请输入用户名:")
        if username in list1:
            print("{}已存在,请更换用户名".format(username))

        # 设置3位及以上密码
        else:
            while True:
                code1 = input("请输入密码:")
                if len(code1) >= 3:
                    code2 = input("请确认密码:")
                    if code1 == code2:
                        with open('./user.txt', 'a+') as f1:
                            f1.write(f'{username}:{code2}\n')
                            f1.seek(0)
                        print("注册成功")
                        break
                    else:
                        print("两次输入不一致,请重新输入")
                else:
                    print("请设置3位以上的密码")
            break

# 登录
def login():
    while True:
        username = input("当前为登录状态,请输入用户名:")
        reader()
        if username in list1:
            n = 0
            inx = list1.index(username)

            # 输入账户被锁定,则重新输入
            if username in list3:
                print("当前用户处于锁定状态,不可登录")
                continue

            # 3次密码输入,登录成功结束程序,否则锁定
            while n <= 2:
                code = input("请输入密码:")
                if list2[inx] == code:
                    print("登陆成功")
                    break
                else:
                    print("密码错误,还有{}次机会".format(2 - n))
                    n += 1

            if n <= 2:
                break

            # 密码3次输入失败
            if n == 3:
                print("密码输入3次失败,账户被锁定")
                lock = list1[inx]
                with open('lock.txt', 'a+', encoding='utf-8') as f2:
                    f2.write(lock + '\n')
                reselection = input("账户被锁定,请选择注册(0)或重新登陆(1):")
                while True:
                    # 注册,登录循环
                    if reselection == '0':
                        register()
                        reader()
                        login()
                        break
                    # 登录循环
                    elif reselection == '1':
                        login()
                        break
                    else:
                        reselection = input("输入错误,请选择注册(0)或重新登陆(1):")
                break

        # 用户名不存在,重新输入
        else:
            r = input("用户名不存在,请选择注册(0)或重新登陆(1):")
            while True:
                if r == '0':
                    register()
                    reader()
                    print(list1)
                    print(list2)
                    print(list3)
                    login()
                    break
                elif r == '1':
                    break
                else:
                    r = input("输入错误,请选择注册(0)或重新登陆(1):")
            if r == '0':
                break


print("程序功能有:\n"
      "1.选择注册或登录\n"
      "2.不能注册重名用户名\n"
      "3.注册两次输入密码需一致,字节应不小于3位\n"
      "4.注册之后可以直接选择登录\n"
      "5.登录时请选择已有账户,若没有账户请选择注册\n"
      "6.登录时若三次输入密码不正确将锁定账户,下次无法登录,请选择其他账户或注册新账户\n")
while True:
    select = input("欢迎加入,请选择注册(0)或登录(1):")
    reader()
    if select == '0':
        # 注册完成之后登录
        register()
        continue
    elif select == '1':
        login()
        break
    print("输入错误,请重新选择")

while True:
    a = input("输入空格并回车结束程序:")
    if a == ' ':
        break
