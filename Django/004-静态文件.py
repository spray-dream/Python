# -*- coding = utf-8 -*-
# @Time : 2022/3/4 14:56
# @Author : spray_dream
# @File : 004-静态文件.py
# @Software: PyCharm
pass
"""
1.在开发过程中,图片,CSS,js都会当作静态文件处理
2.静态文件一般放在app目录下的static文件夹里,该文件夹里一般有:js,img,CSS,plugins等文件夹
3.由于写在HTML里的图片,CSS,js文件的路径全都是绝对路径,类似<img src="/static/img/28062571_p0.jpg" alt="">,
以后想要将静态文件static放到别的地方,需要把所有包含静态文件的路径全都给改一遍,所以推荐django的另一种写法,
在HTML中引入动态文件加载:{% load static %},(写在开头时网页不会出错,但是pycharm会有红色高亮.不写在开头网页就不会出错,但是pycharm有红色高亮)
然后将引入静态文件的语句写成src="{% static '文件路径' %}",比如:<img src="{% static 'img/28062571_p0.jpg' %}" alt="">
<script src="{% static 'js/文件名或js文件夹下的路径' %}"></script>
后面如果需要将static文件放到别处,还需要将settings.py里的STATIC_URL = '/static/'重新配置,这样所有访问静态文件的链接都会被改变
"""

"""
总结003和004:
1.在app目录下创建static文件夹,再创建CSS,img,js,plugins文件夹,分别放入静态文件,
再在app目录下创建templates文件夹,放入user_list.html文件
│  admin.py
│  apps.py
│  models.py
│  tests.py
│  views.py
│  __init__.py
├─ migrations
├─ static
│  ├─CSS
│  ├─img
│  │      28062571_p0.jpg
│  ├─js
│  └─plugins
├─templates
│      user_list.html

2.在views.py里创建函数
def user_list(request):
    return render(request, 'user_list.html')
3.在urls.py里添加路径:path('user/list'.views.user_list),
4.并且html文件里加在路径里写入静态文件时换一种写法:src或href="{% static 'img或CSS或js/文件名' %}"
5.用户请求时输入127.0.0.1:8000/user/list/,程序访问user_list函数,并找到static文件夹下的user_list.html文件,
返回里面的结果,呈现在网页上.
"""
