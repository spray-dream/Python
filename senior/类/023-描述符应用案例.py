# -*- coding = utf-8 -*-
# @Time : 2021/12/14 15:18
# @Author : spray_dream
# @File : 023-描述符应用案例.py
# @Software: PyCharm
pass
"""
要求:学员的分数只能在0到100之间
解决方法:
    1.在__init__方法中检测,但只能在初始化时有效
        if 0 <= score <= 100:
            self.score = score
    2.__setattr__方法,判断在赋值的时候是否符合条件
    3.描述符
"""

# class Student:
#     def __init__(self, id, name, score):
#         self.id = id
#         self.name = name
#         if 0 <= score <= 100:
#             self.score = score
#         else:
#             print('当前分数不正确')
#
#     def returnMe(self):
#         info = f"""
#         学员编号:{self.id}
#         学员姓名:{self.name}
#         学员分数:{self.score}"""
#         print(info)
#
#     def __setattr__(self, key, value):
#         print(key, value)
#         if key == 'score':
#             if 0 <= value <= 100:
#                 object.__setattr__(self, key, value)
#             else:
#                 print('当前分数不正确*')
#         else:
#             object.__setattr__(self, key, value)
#
# s = Student(10, 'spray', 0)
# s.returnMe()
# s.score = -10


# 使用描述符
class Score:
    score = 0

    def __get__(self, instance, owner):
        return self.score

    def __set__(self, instance, value):
        if 0 <= value <= 100:
            self.score = value
        else:
            print('分数不正确')

class Student:
    # 为什么类属性能和实例属性联系起来
    score = Score()

    def __init__(self, id, name, score):
        self.id = id
        self.name = name
        print(Student.score, '1')
        self.score = score
        print(Student.score, '2')
        print(self.score is Student.score)

    def returnMe(self):
        print(Student.score, '3')
        info = f"""
        学员编号:{self.id}
        学员姓名:{self.name}
        学员分数:{self.score}"""
        print(info)


print(Student.score, '4')
s = Student(101, 'spray', 10)
s.returnMe()
s.score = -10
s.returnMe()
print(Student.score, '5')
print(s.score)
