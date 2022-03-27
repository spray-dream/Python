from django import forms
from django.shortcuts import render, redirect
from app01 import models
from app01.utils.pagination import Pagination
from app01.utils.bootstrap import BootStrapModelForm
from django.core.exceptions import ValidationError
from app01.utils.md5 import md5

def admin_list(request):
    """管理员列表"""

    """
    # 也可以用中间件实现
    # 源逻辑
    # 用户在通过url访问此页面时,检查用户是否已登录,已登录就继续访问.未登录,就跳转到登录页面
    # 获取url上的cookie随机字符串,并与session中的比较
    info = request.session.get("info")
    if not info:
        return redirect('/login/')
    """

    # 获取当前登录的管理员的信息:{"id": id, "name": name}
    info_dict = request.session["info"]

    # 搜索框
    # data_dict默认为空,即获取所有的账号列表
    data_dict = {}
    # value默认空字符串,如果输入搜索的值,搜索之后搜索框里显示搜索的值
    value = request.GET.get("q", "")
    if value:
        # 获取包含value的结果
        data_dict["username__contains"] = value

    queryset = models.Admin.objects.filter(**data_dict)
    page_object = Pagination(request, queryset)

    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.html(),
        "value": value,
        "info_dict": info_dict,
    }

    return render(request, 'admin_list.html', context)

class AdminModelForm(BootStrapModelForm):

    confirm_password = forms.CharField(
        label="确认密码",
        # widget=forms.PasswordInput(render_value=True)    # 写错的密码不清空
        widget=forms.PasswordInput
    )

    class Meta:
        model = models.Admin
        fields = ["username", "password", "confirm_password"]
        widgets = {
            # "password": forms.PasswordInput(render_value=True)
            "password": forms.PasswordInput
        }

    # 密码加密
    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)

    # 验证2次密码输入一致
    def clean_confirm_password(self):
        pwd = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirm_password"))
        if confirm != pwd:
            raise ValidationError("密码不一致")
        return confirm

class AdminEditModelForm:
    class Meta:
        model = models.Admin
        fields = ["username"]

def admin_add(request):
    """添加管理员"""

    if request.method == "GET":
        form = AdminModelForm()
        return render(request, 'admin_add.html', {"form": form})

    form = AdminModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        return redirect('/admin_list/')
    return render(request, 'admin_add.html', {"form": form})

def admin_edit(request, nid):
    """编辑管理员"""

    row_object = models.Admin.objects.filter(id=nid).first()
    if not row_object:
        return redirect('/admin_list/')

    if request.method == "GET":
        # 根据传递的id获取那一行的数据
        form = AdminModelForm(instance=row_object)    # instance显示默认值
        return render(request, 'user_edit.html', {'form': form})

    # 保证改变的数据是id=nid的那一行
    form = AdminModelForm(data=request.POST, instance=row_object)

    # 校验数据,保存
    if form.is_valid():
        form.save()
        return redirect('/admin_list/')

    # 校验失败
    return render(request, 'admin_edit.html', {"form": form})

def admin_del(request, nid):
    """删除管理员"""

    models.Admin.objects.filter(id=nid).delete()
    return redirect('/admin_list/')

class AdminResetModelForm(BootStrapModelForm):

    confirm_password = forms.CharField(
        label="确认密码",
        widget=forms.PasswordInput(render_value=True)
    )

    class Meta:
        model = models.Admin
        fields = ["password", "confirm_password"]
        widgets = {
            "password": forms.PasswordInput(render_value=True)
        }

    # 密码加密
    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)

    # 验证2次密码输入一致
    def clean_confirm_password(self):
        pwd = self.cleaned_data.get("password")
        confirm = md5(self.cleaned_data.get("confirm_password"))
        if confirm != pwd:
            raise ValidationError("密码不一致")
        return confirm

def admin_reset(request, nid):
    """重置密码"""

    row_object = models.Admin.objects.filter(id=nid).first()
    if not row_object:
        return redirect('/admin_list/')

    title = "{}".format(row_object.username)
    if request.method == "GET":
        form = AdminResetModelForm()
        return render(request, 'admin_reset.html', {"form": form, "title": title})

    form = AdminResetModelForm(data=request.POST, instance=row_object)
    if form.is_valid():
        form.save()
        return redirect('/admin_list/')
    return render(request, 'admin_reset.html', {"form": form, "title": title})
