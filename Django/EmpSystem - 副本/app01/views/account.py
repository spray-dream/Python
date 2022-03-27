from django import forms
from django.shortcuts import render, redirect, HttpResponse
from app01.utils.md5 import md5
from app01 import models
from app01.utils.pil import check_code
from io import BytesIO

class LoginForm(forms.Form):
    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True   # 表示必填
    )
    password = forms.CharField(
        label="密码",
        widget=forms.PasswordInput(render_value=True),
        required=True
    )
    code = forms.CharField(
        label="验证码",
        widget=forms.TextInput,
        required=True
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 循环ModelForm中的所有字段，给每个字段的插件设置
        for name, field in self.fields.items():
            # 字段中有属性，保留原来的属性，没有属性，才增加。
            if field.widget.attrs:
                field.widget.attrs["class"] = "form-control"
                field.widget.attrs["placeholder"] = field.label
            else:
                field.widget.attrs = {
                    "class": "form-control",
                    "placeholder": field.label
                }

    def clean_password(self):
        pwd = self.cleaned_data.get("password")
        return md5(pwd)


def login(request):
    """登录"""

    if request.method == "GET":
        form = LoginForm()
        return render(request, 'login.html', {"form": form})

    form = LoginForm(data=request.POST)
    if form.is_valid():
        # 验证成功,获取到的用户名和密码
        # {'username': 'xxx', 'password': '123, 'code': 123}

        # 验证码校验
        # 剔除掉 form.clean_data()中的code,因为数据库里不会存储验证码的信息.同时拿到验证码
        user_input_code = form.cleaned_data.pop('code')
        # 获取session中的验证码(可能为空)
        code = request.session.get('image_code', "")
        if code.upper() != user_input_code.upper():
            form.add_error("code", "验证码错误")
            return render(request, 'login.html', {"form": form})

        # 去数据库校验用户和密码是否正确
        admin_object = models.Admin.objects.filter(**form.cleaned_data).first()
        # 验证输入是否为空
        if not admin_object:
            form.add_error("password", "用户名或密码错误")
            return render(request, 'login.html', {"form": form})

        # 正确
        # 生成cookie的随机字符串,并写入session中,
        request.session["info"] = {"id": admin_object.id, "name": admin_object.username}

        # session保存7天
        request.session.set_expiry(60 * 60 * 24 * 7)

        return redirect('/admin_list/')
    return render(request, 'login.html', {"form": form})

def image_code(request):
    """图片验证码"""

    img, code_string = check_code()

    # 写入session中,以便于后续获取验证码再进行校验
    request.session['image_code'] = code_string
    # 给session设置一个60秒超时,过60秒之后失效
    request.session.set_expiry(60)

    # 创建了一个内存文件
    stream = BytesIO()
    # 将图片放入内存文件中
    img.save(stream, 'png')
    # stream.getvalue()    # 从内存中获取图片对象

    return HttpResponse(stream.getvalue())

def logout(request):
    """清除session,退出"""

    request.session.clean()
    return redirect('/login/')
