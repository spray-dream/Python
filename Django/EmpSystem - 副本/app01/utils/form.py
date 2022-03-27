from app01 import models
from django import forms
from django.core.exceptions import ValidationError

class UserModelForm(forms.ModelForm):
    class Meta:
        # 错误提示:ModelForm has no model class specified.
        model = models.UserInfo

        # 设置成fields接收,django.core.exceptions.ImproperlyConfigured: Creating a ModelForm without either
        # the 'fields' attribute or the 'exclude' attribute is prohibited; form UserModelForm needs updating.
        fields = ["name", "password", "sex", "age", "money", "create_time", "dept"]

        # 设置表单文本框样式
        # widgets = {
        #     "name": forms.TextInput(attrs={"class": "form-control"}),
        #     "password": forms.PasswordInput(attrs={"class": "form-control"})
        # }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # 循环找到所有的,并添加标签属性
        for name, i in self.fields.items():
            i.widget.attrs = {"class": "form-control", "placeholder": i.label}


class SuperModelForm(forms.ModelForm):

    # # 导入正则表达式验证格式,方式1
    # mobile = forms.CharField(
    #     label="手机号",
    #     validators=[RegexValidator(r'^\d{11}$', '手机号格式错误')]
    # )

    class Meta:
        model = models.SuperNum
        # fields = ["mobile", "level", "status"]
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, i in self.fields.items():
            i.widget.attrs = {"class": "form-control", "placeholder": i.label}

    # 验证格式方式2,钩子方法,可以编辑更复杂的验证方法
    def clean_mobile(self):
        txt_mobile = self.cleaned_data["mobile"]

        # 验证添加的账号手机号是否已经存在
        exists = models.SuperNum.objects.filter(mobile=txt_mobile).exists()
        if exists:
            raise ValidationError("手机号已存在")

        if len(txt_mobile) != 11:
            raise ValidationError("格式错误")
        return txt_mobile


class SuperEditModelForm(forms.ModelForm):

    # # 手机号可见但不可编辑
    # mobile = forms.CharField(disabled=True, label="手机号")

    class Meta:
        model = models.SuperNum
        fields = ["mobile", "level", "status"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for name, i in self.fields.items():
            i.widget.attrs = {"class": "form-control", "placeholder": i.label}

    # 验证格式
    def clean_mobile(self):
        txt_mobile = self.cleaned_data["mobile"]
        # 获取除了当前编辑的一行的id外已经存在的手机号
        exists = models.SuperNum.objects.exclude(id=self.instance.pk).filter(mobile=txt_mobile).exists()
        if exists:
            raise ValidationError("手机号已存在")
        return txt_mobile
