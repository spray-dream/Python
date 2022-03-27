from django.shortcuts import render, redirect
from app01 import models
from app01.utils.pagination import Pagination
from app01.utils.form import UserModelForm

def user_list(request):
    """用户列表"""

    # 获取所有的的用户列表
    queryset = models.UserInfo.objects.all()

    # 分页组件
    page_object = Pagination(request, queryset)
    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.html()
    }

    # 在模板语法中方法不加括号
    # i.get_sex_display()显示性别元组里替代的原本数据
    # i.create_time.strftime(now())将日期格式转换成字符串||在模板中使用过滤器{ i.create_time|date:'Y-m-d H:i:s' }
    # i.dept.title直接根据外键获取对应的名称
    return render(request, 'user_list.html', context)

def user_add_1(request):
    """新建用户(原始写法)"""

    if request.method == "GET":
        text = {
            'gender_choices': models.UserInfo.gender_choices,
            'dept_list': models.Department.objects.all()
        }
        return render(request, 'user_add_1.html', text)

    # 真的好麻烦,用户填写的数据还可能需要进行验证,以及填写错误时的错误提示,过于繁复
    # user = request.POST.get("name")
    # pwd = request.POST.get("pwd")
    # sex = request.POST.get("sex")
    # age = request.POST.get("age")
    # money = request.POST.get("money")
    # create_time = request.POST.get("create_time")
    # dept = request.POST.get("dept_title")
    #
    # models.UserInfo.objects.create(name=user, password=pwd, sex=sex, age=age, money=money,
    #                                create_time=create_time, dept=dept)

    redirect("/user_list/")

def user_add(request):
    """modelform新建用户"""

    # url请求,返回新建用户页面
    if request.method == "GET":
        form = UserModelForm()
        return render(request, 'user_add.html', {"form": form})

    # 获取提交的表单数据
    form = UserModelForm(data=request.POST)
    # 校验数据
    if form.is_valid():
        # print(form.cleaned_data)    # 获得提交的数据的字典形式

        # models.UserInfo.objects.create()
        form.save()
        return redirect('/user_list/')

    # 校验失败
    return render(request, 'user_add.html', {"form": form})

def user_edit(request, nid):
    """编辑用户"""

    if request.method == "GET":
        # 根据传递的id获取那一行的数据
        row_object = models.UserInfo.objects.filter(id=nid).first()

        form = UserModelForm(instance=row_object)
        return render(request, 'user_edit.html', {'form': form})

    # 保证改变的数据是id=nid的那一行
    row_object = models.UserInfo.objects.filter(id=nid).first()
    form = UserModelForm(data=request.POST, instance=row_object)

    # 校验数据,保存
    if form.is_valid():
        form.save()
        return redirect('/user_list/')

    # 校验失败
    return render(request, 'user_edit.html', {"form": form})

def user_del(request, nid):
    """删除用户"""

    models.UserInfo.objects.filter(id=nid).delete()
    return redirect('/user_list/')
