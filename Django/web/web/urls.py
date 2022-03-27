"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from myhome import views
# from myhome import urls as app_urls    # 引入子路由文件

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index),
    path('tpl/', views.tpl),
    path('tpl_syntax/', views.tpl_syntax),
    path('myobject/', views.myobject),
    path('myfor/', views.myfor),
    path('mymo/', views.mymo),
    # path('', include('myhome.urls'))    # include是加载子目录app目录下的子路由文件的
    path('login/', views.login),
    path('info_list/', views.info_list),
    path('info_add/', views.info_add),
    path('info_del/', views.info_del),
]
