from django.db import models

class Admin(models.Model):
    """管理员"""
    objects = models.Manager()
    username = models.CharField(verbose_name="用户名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=64)

    def __str__(self):
        return self.username


class Department(models.Model):
    """部门表"""
    objects = models.Manager()
    title = models.CharField(verbose_name="标题", max_length=64)

    def __str__(self):
        return self.title


class UserInfo(models.Model):
    """员工表"""
    objects = models.Manager()
    name = models.CharField(verbose_name="姓名", max_length=32)
    password = models.CharField(verbose_name="密码", max_length=16)

    gender_choices = (
        (1, "男"),
        (0, "女")
    )
    sex = models.SmallIntegerField(verbose_name="性别", choices=gender_choices)

    age = models.IntegerField(verbose_name="年龄")
    money = models.DecimalField(verbose_name="工资", max_digits=10, decimal_places=2, default=0)
    create_time = models.DateField(verbose_name="入职时间")

    # dept字段在数据库中自动生成dept_id的字段名
    # 1.给外键字段设置级联删除:on_delete=models.CASCADE.2.或者置空
    dept = models.ForeignKey(verbose_name="所属部门", to="Department", to_field="id", null=True,
                             blank=True, on_delete=models.SET_NULL)


class SuperNum(models.Model):
    """高级账号"""
    objects = models.Manager()
    mobile = models.CharField(verbose_name="手机号", max_length=11)
    level_choices = (
        (1, "1级"),
        (2, "2级"),
        (3, "3级"),
        (4, "4级"),
    )
    level = models.SmallIntegerField(verbose_name="级别", choices=level_choices, default=1)

    status_choices = (
        (1, "已占用"),
        (2, "未使用")
    )
    status = models.SmallIntegerField(verbose_name="状态", choices=status_choices, default=2)


class Task(models.Model):
    """任务"""
    objects = models.Manager()
    title = models.CharField(verbose_name="标题", max_length=64)
    detail = models.TextField(verbose_name="详细信息")
    level_choices = (
        (1, "紧急"),
        (2, "重要"),
        (3, "临时"),
    )
    level = models.SmallIntegerField(verbose_name="级别", choices=level_choices, default=3)
    user = models.ForeignKey(verbose_name="负责人", to="Admin", on_delete=models.CASCADE)
