from django.shortcuts import render, redirect
from app01 import models
from app01.utils.pagination import Pagination

def dept_list(request):
    """部门列表"""

    # 去数据库中获取所有的部门列表
    queryset = models.Department.objects.all()

    # 分页
    page_object = Pagination(request, queryset)
    context = {
        "queryset": page_object.page_queryset,
        "page_string": page_object.html()
    }

    # 将列表写在HTML中,并遍历展现在页面上
    return render(request, 'dept_list.html', context)

def dept_add(request):
    """添加部门"""

    if request.method == "GET":
        return render(request, 'dept_add.html')
    # 获取用户提交的数据name="title",value="???"
    title = request.POST.get("title")
    # 在数据库中添加title的值
    models.Department.objects.create(title=title)
    # 重定向回部门列表
    return redirect("/dept_list/")

def dept_del(request):
    """删除部门"""

    # 通过获取页面上部门列表中对应的删除键链接上的nid得到对应的ID
    nid = request.GET.get('nid')
    # 删除该ID对应的一行数据
    models.Department.objects.filter(id=nid).delete()
    # 重定向回部门列表
    return redirect("/dept_list/")

def dept_edit(request):
    """编辑部门"""

    # 自己理解的过程:在dept_list/点击编辑之后,[09/Mar/2022 17:51:22] "GET /dept_edit/?nid=2 HTTP/1.1" 200 2989,
    # 应该是由dept_list.html的链接访问dept_edit/页面,调用edit函数,并传递了nid=id(值),
    # 函数获取到,然后传给edit的HTML,编辑完title的value点了提交后,
    # 几乎同时进行了命令行的以下两步:[09/Mar/2022 17:51:51] "POST /dept_edit/?nid=2 HTTP/1.1" 302 0
    # 这里没有写明action,是提交给了edit本身的url,然后继续由url(method=post)再次访问函数edit,并获取title更新数据库
    # 最后重定向list页面:[09/Mar/2022 17:51:51] "GET /dept_list/ HTTP/1.1" 200 4058

    # 也可以对url使用正则
    nid = request.GET.get('nid')
    if request.method == "GET":
        # 根据提交的nid = id,获取这一行数据
        row_obj = models.Department.objects.filter(id=nid).first()
        return render(request, 'dept_edit.html', {"row_obj": row_obj})
    # 获取用户提交的标题数据
    title = request.POST.get("title")
    # 根据ID找到数据库的数据并进行更新
    models.Department.objects.filter(id=nid).update(title=title)
    return redirect("/dept_list/")
