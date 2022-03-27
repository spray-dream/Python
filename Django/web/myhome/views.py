from django.shortcuts import render, HttpResponse, redirect
from . import models
from django.forms import Form
from django import forms
from .models import Stu

# Create your views here.
def index(request):
    # request其实是一个对象,封装了用户发送过来的所有请求相关的数据
    print(request.method)
    print(request.GET)
    print(request.POST)
    # return HttpResponse('欢迎使用')
    return redirect("http://www.baidu.com")    # 重定向

def tpl(request):
    return render(request, 'tpl.html')

def tpl_syntax(request):
    r1 = request.method
    r2 = request.GET
    r3 = request.POST
    my_str = 'string'
    my_int = 11
    my_list = [1, 2, 3]
    my_list2 = [
        {'name': 'python', 'age': 18},
        {'name': 'python', 'age': 18},
        {'name': 'python', 'age': 18}
    ]
    my_tup = (1, 2, 3)
    my_dic = {'name': 'python', 'age': 18}
    my_set = {1, 3, 4}
    my_bool = True
    my_float = 11.11
    return_dic = {
        'str': my_str,
        'int': my_int,
        'list': my_list,
        'list2': my_list2,
        'dict': my_dic,
        'tuple': my_tup,
        'set': my_set,
        'bool': my_bool,
        'float': my_float,
        'r1': r1,
        'r2': r2,
        'r3': r3,
    }
    return render(request, 'tpl_syntax.html', return_dic)

def myobject(request):

    def func():
        print('我是func')
        return 'func'

    class Class():
        def get_self(self):
            return 'self'

        @staticmethod
        def static():
            return 'static'

        @classmethod
        def class_method(cls):
            return cls

        # 打印类/对象是自动触发，代替对象的内存地址
        # def __str__(self):
        #     return '我是谁？'
    obj = Class()
    return render(request, 'myobject.html', locals())

def myfor(request):
    my_str = 'string'
    my_dic = {'name': 'python', 'age': 18}
    my_list = []
    my_if = 0
    return render(request, 'myfor.html', locals())

def mymo(request):
    # 1.增
    # obj = models.Stu()
    # obj.name = 'zhangsan'
    # obj.age = 20
    # obj.sex = 1
    # obj.address = 'shandong'
    # obj.save()

    # data = {'name': 'lisi', 'age': 22, 'sex': 0, 'address': 'shanxi'}
    # obj = models.Stu(**data)
    # obj.save()

    # models.Department.objects.create(title="销售部")
    # models.Department.objects.create(title="IT")
    # models.Department.objects.create(title="运营部")

    # 2.删
    # models.Stu.objects.filter(id=3).delete()  # filter相当于where
    # models.Stu.objects.all().delete()

    # 3.查
    # data_list1 = models.Stu.objects.all()
    # print(data_list1)
    # for i in data_list1:
    #     print(i.id, i.name, i.age)

    # data_list2 = models.Stu.objects.filter(id=1)
    # print(data_list2)
    # for i in data_list2:
    #     print(i.id, i.name, i.age)

    # data_list3 = models.Stu.objects.first()
    # print(data_list3)
    # print(data_list3.id, data_list3.name, data_list3.age)

    # 4.改
    # models.Stu.objects.all().update(age=30)
    # models.Stu.objects.filter(id=5).update(age=10)

    return HttpResponse("成功")

def login(request):
    if request.method == "GET":
        return render(request, 'login.html')

    # 如果是POST请求,获取用户提交的数据

    # 1.自己的理解:用户先通过url访问函数,并返回登陆界面的HTML,提交数据(method=post)之后数据以request方式打包成一个参数,
    # 2.然后后台程序能再次访问该函数,能以request.POST.get("name")的方式获取提交的数据
    # 3.如果想要获取某个用户想要操作的对象的定位id以便能对这个关联的数据进行操作,
    # 4.可以使用<a href="/url/?变量名nid={{ id }}">点我跳转链接</a>,这样就能在函数中使用url传递的name=value,
    # 5.然后就能通过request.GET.get("nid")获取nid的值id了
    print(request.POST)
    username = request.POST.get("username")
    password = request.POST.get("pwd")
    if username == "root" and password == "123":
        # return HttpResponse("登录成功")
        return redirect("http://www.baidu.com")

    # return HttpResponse("登陆失败")
    return render(request, 'login.html', {"error_msg": "登录失败"})


def info_list(request):
    # 1.获取数据库中的信息
    data_list = models.Stu.objects.all()
    return render(request, 'info_list.html', {"data_list": data_list})

def info_add(request):
    # 2.用户提交数据,写入数据库
    if request.method == "GET":
        return render(request, 'info_add.html')
    username = request.POST.get("username")
    password = request.POST.get("pwd")
    age = request.POST.get("age")

    # 3.添加到数据库
    models.Stu.objects.create(name=username, password=password, age=age)
    # return HttpResponse("成功")
    return redirect("/info_add/")

def info_del(request):
    # 4.删除用户点击的数据
    nid = request.GET.get('nid')
    models.Stu.objects.filter(id=nid).delete()
    return redirect("/info_list/")


# form组件
class MyForm(Form):
    user = Form.CharFile(widget=Form.Input)
    pwd = Form.CharFile(widget=Form.Input)
    email = Form.CharFiled(widget=Form.Input)

def u_add(request):
    if request == "GET":
        form = MyForm()
        return render(request, 'u_add.html', {"form": form})


# ModelForm组件,更简洁
class ModForm(forms.ModelForm):
    xx = Form.Charfile("....")    # 也可以自定义model类里没有的字段

    class Meta:
        model = Stu
        fields = ["name", "password", "age", "sex", "address", "size", "...."]
