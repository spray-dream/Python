# -*- coding = utf-8 -*-
# @Time : 2022/3/8 0:12
# @Author : spray_dream
# @File : 007-数据库操作.py
# @Software: PyCharm
pass
"""
注意:在models中需要给每个类添加一个objects = models.Manage(),不然会有黄色语法提示
"""

"""
增:
给表字段添加值,实际中是接收用户传来的数据并给字段添加值
一.在views视图中
1.首先在views.py中导入定义好的模型类:from . import models,然后创建处理数据的函数.记得写返回值
2.添加值的方法:
(1)将类实例化成obj,并给每个字段添加值:依次给实例化对象的属性赋值:obj.name = "zhangsan"......
最后实例化的对象调用save()方法保存
(2)使用字典方式:
data = {'name': 'lisi', 'age': 22, 'sex': 0, 'address': 'shanxi'}
obj = models.Stu(**data)
obj.save()
最后一定要obj.save()保存,不然数据不会更新(卡住之后添加了好几次数据???)
(3)直接用models.类名(表).objects.create(字段名1="值1", 字段名2="值2", 字段名3="值3")
二.可以直接在models.py中类名(表).objects.create(字段名1="值1", 字段名2="值2", 字段名3="值3"),然后迁移
"""

"""
删:
在view的函数中
1.删除某条数据:models.类名.objects.filter(id=3).delete()    # filter相当于where
2.删除整张表的数据:models.类名.objects.all().delete()
"""

"""
查:
在view函数中
1.select * from 表名;
models.类名.objects.all()    # 获取到的是一个QuerySet列表的类型
[<Stu: Stu object (1)>, <Stu: Stu object (5)>]列表里每一个元素相当于一个对象即一行数据.
可以用for循环取出:
data_list = models.Stu.objects.all()
print(data_list)
for i in data_list:
    print(i.id, i.name, i.age)
2.select * from 表名 where id = 1;
data_list2 = models.Stu.objects.filter(id=1)
print(data_list2)
for i in data_list2:
    print(i.id, i.name, i.age)
3.取出第一行数据:
select * from 表名 limit 1;
data_list3 = models.Stu.objects.first()
print(data_list3)
print(data_list3.id, data_list3.name, data_list3.age)
"""

"""
改:
在view函数中
1.将某字段的值全部修改
models.Stu.objects.all().updata(age=30)
2.修改某条:
models.Stu.objects.filter(id=5).update(age=10)
"""
