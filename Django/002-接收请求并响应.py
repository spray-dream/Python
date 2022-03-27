# -*- coding = utf-8 -*-
# @Time : 2022/3/3 22:21
# @Author : spray_dream
# @File : 002-接收请求并响应.py
# @Software: PyCharm
pass
"""
1.确保app已注册
2.编写URL和视图函数对应关系:
    在urls.py中有一个默认的:
urlpatterns = [
    path('admin/', admin.site.urls),
]
    可以将path('admin/', admin.site.urls),先注释掉换上自己的:path('index/', admin.site.urls),
    如果用户在访问时输入了一个类似的网址:www.xxx.com/index/,就会执行后面admin.site.urls的函数.函数一般写在views.py里.
    这时候就需要在urls.py里导入,from myhome import views,然后换上('index/', views.index),表示只要用户访问上面index/网址,
    就会去views.py文件中访问并执行index函数
3.编写视图函数,在views.py中
小bug:
    当web这个项目单独用pycharm打开时可以直接在urls.py中用绝对导入,而不会有语法红色警告.而web作为其他项目的子文件夹时会显示.
    以及不知道为什么不能用相对导入,报错:ImportError: attempted relative import beyond top-level package
    (超出了顶层package进行相对导入)
4.用户只要访问这个网址:127.0.0.1:8000/index/就能看到结果
"""

"""
总结001和002:
1.创建项目django-admin startproject 项目名称(英文)
2.启动项目python manage.py runserver,并在浏览器中输入url:127.0.0.1:8000/
3.创建应用python manage.py startapp myhome
4.在settings.py中的INSTALLED_APPS后面添加'myhome.apps.MyhomeConfig'确保app注册
5.在views.py中添加函数,可以起函数名为index,参数必须为request:
    def index(request):
        return HttpResponse('欢迎使用')
6.在urls.py中写上从myhome中导入views.py这个模块,即from myhome import views,并在urlpatterns添加path('index/',views.index),
    views.index表示views模块中的index函数
7.用户输入url:127.0.0.1:8000/index/就能看到最终结果,return HttpResponse()的一行文字

8.之后就可以重复添加函数与添加路径的过程了:
    views.py:
        def user_list(request):
            return HttpResponse('用户列表')
        
        def user_add(request):
            return HttpResponse('添加用户')
    urls.py:
        path('user/list/', views.user_list),
        path('user/add/', views.user_add),

10.注意:用127.0.0.1只能进行本地访问,远程访问:python manage.py runserver 0.0.0.0:8000
之后输入本地ip地址10.9.169.253,再加:8000
此时是不允许这个主机名来请求访问,需要将主机地址添加到settings.py中的ALLOWED_HOSTS."*"是通配符,代表任何ip都能访问本项目

连接数据库:在settings.py里的DATABASES里将MySQL连接上:    
'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'test001',
    'USER': 'root',
    'PASSWORD': '340915',
    'HOST': 'localhost',
    'PORT': '3306',
}

11.获取提交表单时的方式(明文GET或POST不可见)
request.method
结果可能是GET或POST
12.获取url传递的name,value值
request.GET或request.POST

13.用户登录:login/
def login(request):
    if request.method == "GET":
        return render(request, 'login.html')
    else:
        # 如果是POST请求,获取用户提交的数据
        print(request.POST)
        return HttpResponse("登录成功")
必须在login.html的form表单中添加{% csrf_token %},不然会出现CSRF错误
过程:用户在访问url时,先以GET方式看到login页面,输入数据后再以post形式输入login/地址,再执行login函数
"""

"""
14:如果想要在页面上编辑完数据并提交给后台即有POST请求, 需要加入判断条件if request.method == "GET":, 并在if里面加上
row_obj = models.Department.objects.filter(id=nid).first()
return render(request, 'dept_edit.html', {"row_obj": row_obj})
类似这样的,从数据库获取数据并返回给前端页面展示出来,然后提交数据的时候会再次访问action里的地址,访问对应的函数,此时是POST请求,
所以可以用title = request.POST.get("title")获取提交的数据?title=IT部,并在在数据库中添加title的值:
models.Department.objects.create(title=title)
"""
