# -*- coding = utf-8 -*-
# @Time : 2022/2/13 19:30
# @Author : spray_dream
# @File : controllerclass.py
# @Software: PyCharm

"""
操作控制类
"""
import random

class Controller:

    def reader(self):
        global list1, list2, list3, list4, list5, list6
        list1 = []
        list2 = []
        list3 = []
        list4 = []
        list5 = []
        list6 = []
        list7 = []
        with open('./data/user.txt', 'a+', encoding='utf-8') as f1:
            f1.seek(0)
            content1 = f1.readlines()
            print("用户有:", content1)
            for i in content1:
                i = i.replace('\n', '')
                i = i.split(':')
                list1.append(i[0])
                list2.append(i[1])
        with open('./data/lock.txt', 'a+', encoding='utf-8') as f2:
            f2.seek(0)
            content2 = f2.readlines()
            print("被锁定用户有:", content2)
            for i in content2:
                i = i.replace('\n', '')
                list3.append(i)
        with open('./data/userid.txt', 'a+', encoding='utf-8') as f3:
            f3.seek(0)
            content3 = f3.readlines()
            print("身份证,卡号和phone有:", content3)
            for i in content3:
                i = i.replace('\n', '')
                i = i.split(':')
                list4.append(i[0])
                list5.append(i[1])
                list7.append(i[2])
        with open('./data/money.txt', 'a+', encoding='utf-8') as f4:
            f4.seek(0)
            content4 = f4.readlines()
            print("余额有:", content4)
            for i in content4:
                i = i.replace('\n', '')
                list6.append(i)

    # 1.注册
    def register(self):
        while True:

            # 1.录入身份证号
            user_id = input('输入身份证号:')
            if str.isdigit(user_id):
                pass
            else:
                print('输入的不是数字,重新输入')
                continue
            if user_id in list4:
                print("{}已存在".format(user_id))
                m = input('选择(0)重新输入或其他结束注册')
                if m == '0':
                    pass
                else:
                    break
            elif len(user_id) != 3:
                print('身份证号长度不是18位,重新输入')
            elif len(user_id) == 3:
                print('身份证号录入成功')
                card_id = random.randint(100, 999)
                print(f'生成卡号{card_id}')

                # 2.录入手机号
                while True:
                    phone = input('输入11位手机号:')
                    if str.isdigit(phone):
                        pass
                    elif not str.isdigit(phone):
                        print('输入的不是数字,重新输入')
                        continue
                    if len(phone) != 3:
                        print('手机号长度不是11位,重新输入')
                        continue
                    elif len(phone) == 3:
                        break

                # 3.录入用户名
                while True:
                    name = input('输入用户名:')
                    if name in list1:
                        print("{}已存在,请更换用户名".format(name))

                    # 4.设置3位及以上密码
                    else:
                        while True:
                            code1 = input("请输入密码:")
                            if len(code1) >= 3:
                                code2 = input("请确认密码:")
                                if code1 == code2:
                                    with open('./data/userid.txt', 'a+', encoding='utf-8') as f1:
                                        f1.write(f'{user_id}:{card_id}:{phone}\n')
                                        f1.seek(0)
                                    with open('./data/user.txt', 'a+', encoding='utf-8') as f2:
                                        f2.write(f'{name}:{code2}\n')
                                        f2.seek(0)
                                    with open('./data/money.txt', 'a+', encoding='utf-8') as f3:
                                        money = '0'
                                        f3.write(money+'\n')
                                        f3.seek(0)
                                    print("注册成功")
                                    self.reader()
                                    break
                                else:
                                    print("两次输入不一致,请重新输入")
                            else:
                                print("请设置3位以上的密码")
                        break
                break

    # 登录
    def login(self):

        while True:
            name = input("当前为登录状态,输入用户名:")
            if name in list1:
                n = 0
                inx = list1.index(name)

                # 输入账户被锁定,则重新输入
                if name in list3:
                    m = input("当前用户处于锁定状态,不可操作,请选择(0)退出或任意键选择重新输入")
                    if m == 0:
                        break
                    continue

                # 3次密码输入,登录成功结束程序,否则锁定
                while n <= 2:
                    code = input("请输入密码:")
                    if list2[inx] == code:
                        print("登入成功")
                        break
                    else:
                        print("密码错误,还有{}次机会".format(2 - n))
                        n += 1

                if n <= 2:
                    print('name:', name)
                    return name

                # 密码3次输入失败
                if n == 3:
                    print("密码输入3次失败,账户被锁定")
                    lock = list1[inx]
                    with open('./data/lock.txt', 'a+', encoding='utf-8') as f2:
                        f2.write(lock + '\n')
                        f2.seek(0)
                        self.reader()
                    res = input("账户被锁定,请选择退出(0)或登入其他账户(1):")
                    while True:
                        if res == '0':
                            break
                        # 登录循环
                        elif res == '1':
                            self.login()
                            break
                        else:
                            res = input("输入错误,重新选择")
                    break

            # 用户名不存在,重新输入
            else:
                print('name:', name)
                r = input("用户名不存在,请选择退出(0)或登入其他账户(1):")
                while True:
                    if r == '0':
                        break
                    elif r == '1':
                        break
                    else:
                        r = input("输入错误")
                if r == '0':
                    break

    # 2.查询
    def query(self):
        name = self.login()
        print('name:', name)
        if name:
            inx = list1.index(name)
            money = list6[inx]
            print(f'当前余额为{money}')

    # 3.取款
    def get(self):
        name = self.login()

        if name:
            inx = list1.index(name)
            money = eval(list6[inx])
            get_money = 0
            while True:
                get_money = input('输入金额:')
                if money == 0:
                    print('余额为0,请退出重新操作')
                    break
                if str.isdigit(get_money):
                    get_money = eval(get_money)
                    if get_money <= 0:
                        print('金额不超过0,请重新输入')
                        continue
                    if get_money <= money:
                        money = money - get_money
                        list6[inx] = str(money)
                        with open('./data/money.txt', 'w+', encoding='utf-8') as f1:
                            for i in list6:
                                f1.write(i + '\n')
                        print(f'操作成功,余额为{money}')
                        self.reader()
                        break
                    else:
                        print('余额不足,请重新输入:')
                else:
                    print('输入的不是数字,请重新输入:')
            return get_money, name

    # 4.存款
    def add(self):
        name = self.login()

        if name:
            inx = list1.index(name)
            money = eval(list6[inx])

            while True:
                add_money = input('输入存款金额:')
                if str.isdigit(add_money):
                    add_money = eval(add_money)
                    if add_money <= 0:
                        print('金额不超过0,请重新输入')
                        continue
                    money = money + add_money
                    list6[inx] = str(money)
                    print(list6)
                    with open('./data/money.txt', 'w+', encoding='utf-8') as f1:
                        for i in list6:
                            f1.write(i + '\n')
                    print(list6)
                    print(f'存款成功,当前余额为{money}')
                    self.reader()
                    break
                else:
                    print('输入的不是数字,请重新输入:')

    # 5.转账
    def transfer(self):
        trans_m, name = self.get()

        while True:
            person = input('输入转账人的用户名:')
            if (person in list1) and (person != name):
                break
            elif person not in list1:
                print('转账用户不存在,重新输入:')
            if person == name:
                print('不能给自己转账,重新输入:')

        if name:
            if trans_m == '0':
                return
            inx1 = list1.index(person)
            money1 = eval(list6[inx1])
            money1 = money1 + trans_m
            list6[inx1] = str(money1)
            print(list6)
            with open('./data/money.txt', 'w+', encoding='utf-8') as f1:
                for i in list6:
                    f1.write(i + '\n')
            print('转账成功')
            self.reader()

    # 6.锁卡
    def lock(self):
        if not list1:
            print('无可用账户,请先返回注册')
            return

        while True:
            res = input('选择使用(0)密码或(1)身份证号进行锁卡:')
            if res == '0':
                while True:
                    name = input('请输入需要锁卡的用户名:')
                    if name in list1:
                        while True:
                            code = input('请输入密码:')
                            inx = list1.index(name)
                            if code == list3[inx]:
                                with open('./data/lock.txt', 'a+', encoding='utf-8')as f1:
                                    f1.write(name + '\n')
                                    f1.seek(0)
                                print(f'用户名{name}的账户锁定成功')
                                break
                            else:
                                print('密码不正确,重新输入')
                    else:
                        print('该账户不存在,请重新输入')
                    break
            elif res == '1':
                while True:
                    user_id = input('输入身份证号:')
                    if user_id in list4:
                        inx = list4.index(user_id)
                        name = list1[inx]
                        with open('./data/lock.txt', 'a+', encoding='utf-8') as f1:
                            f1.write(name + '\n')
                            f1.seek(0)
                        print(f'身份证号为{user_id}的账户锁定成功')
                        break
                    else:
                        print('该账户不存在,请重新输入')
            else:
                print('输入错误,请重新选择')

    # 7.解卡
    def unlock(self):
        while True:
            user_id = input('输入身份证号:')
            if user_id in list4:
                inx = list4.index(user_id)

    # 8.补卡
    def new_c(self):
        pass

    # 9.改密
    def change(self):
        pass

    # 10.退出
    def save(self):
        pass
