from django.db import models

# Create your models here.
class Stu(models.Model):
    objects = models.Manager()
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=16,null=True)
    age = models.IntegerField(default=21)
    sex = models.CharField(max_length=1, default=0)
    address = models.CharField(max_length=50, null=True)
    # 如果某个字段不想要了,直接注释掉,再执行迁移,会将直接删除
    # 添加新字段的话,如果直接size = models.CharField()并执行迁移,命令行会有提示选择1:直接在命令行输入一个值给所有字段添加这个默认值
    # 2:修改代码,在代码size字段上添加default = 值
    # 如果添加字段时默认为空也可以
    size = models.CharField(max_length=3)

    """
    create myhome_Stu(
        id bigint primary key auto_increment,
        name varchar(20),
        age int default 21
        sex varchar(1) default 0
        address varchar(50) null
        );
    """

    # def __repr__(self):
    #     # return '<Stu: Stu object (1)'    # 默认返回的
    #     return f'<Stu: Stu object (id: {self.id}, name: {self.name})>'

class Department(models.Model):
    objects = models.Manager()
    title = models.CharField(max_length=16)

# 给表Department的字段添加数据,直接在这里写,之后迁移,也能成功
# insert into myhome_Department(title) value("销售部");
# Department.objects.create(title="销售部")
#
# Stu.objects.create(name="spray", age=23, sex=1, size=2)
