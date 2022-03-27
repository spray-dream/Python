"""EmpSystem URL Configuration

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
from django.urls import path
from app01.views import dept, user, super, admin, account, task

urlpatterns = [
    # path('admin/', admin.site.urls),

    # 登录和退出
    path('login/', account.login),
    path('image_code/', account.image_code),
    path('logout/', account.logout),

    # 管理员
    path('admin_list/', admin.admin_list),
    path('admin_add/', admin.admin_add),
    path('admin_edit/<int:nid>', admin.admin_edit),
    path('admin_del/<int:nid>', admin.admin_del),
    path('admin_reset/<int:nid>', admin.admin_reset),

    # 部门
    path('dept_list/', dept.dept_list),
    path('dept_add/', dept.dept_add),
    path('dept_del/', dept.dept_del),
    path('dept_edit/', dept.dept_edit),

    # 用户
    path('user_list/', user.user_list),
    path('user_add_1/', user.user_add_1),
    path('user_add/', user.user_add),
    path('user_edit/<int:nid>', user.user_edit),
    path('user_del/<int:nid>', user.user_del),

    # 高级账号
    path('super_list/', super.super_list),
    path('super_add/', super.super_add),
    path('super_edit/<int:nid>', super.super_edit),
    path('super_del/<int:nid>', super.super_del),

    # 任务
    path('task_list/', task.task_list),
    path('task_ajax/', task.task_ajax),
    path('task_add/', task.task_add),
]
