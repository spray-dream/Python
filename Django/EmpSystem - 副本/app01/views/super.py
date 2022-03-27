from django.shortcuts import render, redirect
from app01 import models
from app01.utils.pagination import Pagination
from app01.utils.form import SuperModelForm, SuperEditModelForm

def super_list(request):
    """高级账号列表"""

    # 搜索
    # data_dict默认为空,即获取所有的账号列表
    data_dict = {}
    # value默认空字符串,如果输入搜索的值,搜索之后搜索框里显示搜索的值
    value = request.GET.get("q", "")
    if value:
        # 获取包含value的结果
        data_dict["mobile__contains"] = value

    """
    # 分页
    '''
    分页说明:首先限制每页的行数page_size,然后将每页应显示的数据和当前页面页码以get方式传到前端,并给每页的页码图层设置限制(>0,<=总页码数)
    并添加上下页和跳转页码显示
    '''
    # 默认page=1,限制每页展示的行数
    page = int(request.GET.get('page', 1))
    page_size = 10
    start = (page - 1) * page_size
    end = page * page_size

    # 获取超级账号信息,并以级别高的排在前面
    queryset = models.SuperNum.objects.filter(**data_dict).order_by("-level")[start:end]

    # 得到总条数,即数据库多少行数据
    total_count = models.SuperNum.objects.filter(**data_dict).order_by("-level").count()
    total_page, div = divmod(total_count, page_size)
    # 总条数%每页展示多少条数据,余数不为0时页码向上取整
    if div:
        total_page += 1

    # 计算并显示当前页码的前5个和后5个
    plus = 5
    # 当页码数较少时,直接展示前11个
    if total_page <= 2 * plus + 1:
        start_page = 1
        end_page = total_page

    # 当数据库中数据较多时,大于11
    else:
        # 当前页码<=5时,页码从1开始
        if page <= plus:
            start_page = 1
            end_page = 2 * plus + 1

        # 页码大于5时,直接显示前5个和后5个
        else:
            # 当前页码+plus>总页码时,需要限制极值
            if (page + plus) > total_page:
                start_page = 1
                end_page = total_page
            else:
                start_page = page - plus
                end_page = page + plus

    # 页码
    page_str_list = []

    # 首页
    page_str_list.append('<li><a href="?page=1">首页</a></li>'.format(1))
    # 上一页
    if page > 1:
        prev = '<li><a href="?page={}">上一页</a></li>'.format(page - 1)
    # 限制页码是1时上一页的链接
    else:
        prev = '<li><a href="?page={}">上一页</a></li>'.format(1)
    # 将上一页的标签和链接添加到页码图层最左边
    page_str_list.append(prev)

    # 当前列表页面显示的页码
    for i in range(start_page, end_page + 1):
        if i == page:
            # 用颜色突出当前页码
            ele = '<li class="active"><a href="?page={}">{}</a></li>'.format(i, i)
        else:
            # 当前页遍历开始页码和结束页码通过前端标签显示,并通过链接以get方式传递?page=i以跳转到i页码
            ele = '<li><a href="?page={}">{}</a></li>'.format(i, i)
        page_str_list.append(ele)

    # 下一页
    if page < total_page:
        prev = '<li><a href="?page={}">下一页</a></li>'.format(page + 1)
    # 限制页码是total_page时下一页的链接
    else:
        prev = '<li><a href="?page={}">下一页</a></li>'.format(total_page)
    # 将上一页的标签和链接添加到页码图层最右边
    page_str_list.append(prev)
    # 尾页
    page_str_list.append('<li><a href="?page={}">尾页</a></li>'.format(total_page))

    # 输入跳转页码
    searching_string =
    '''
    <li>
        <form style="float: left; margin-left: -1px" method="get">
            <div class="input-group" style="width: 200px">
                <input name="page"
                       type="text" class="form-control" placeholder="页码" style="position: relative;
                       float: left; display: inline-block; width: 80px; border-radius: 0;">
                <button style="border-radius: 0" class="btn btn-default" type="submit">跳转</button>
            </div>
        </form>
    </li>
    '''
    page_str_list.append(searching_string)

    # 将页码图层添加到html中
    page_string = mark_safe("".join(page_str_list))

    return render(request, 'super_list.html', {"queryset": queryset, "value": value, "page_string": page_string})
    """

    # 获取账号信息,并以级别高的排在前面
    queryset = models.SuperNum.objects.filter(**data_dict).order_by("-level")

    # 实例化分页的类
    page_object = Pagination(request, queryset)
    page_queryset = page_object.page_queryset
    page_string = page_object.html()
    context = {"queryset": page_queryset, "value": value, "page_string": page_string}
    return render(request, 'super_list.html', context)

def super_add(request):
    """账号添加"""

    if request.method == "GET":
        form = SuperModelForm()
        return render(request, "super_add.html", {"form": form})

    # 获取提交的表单数据
    form = SuperModelForm(data=request.POST)
    # 校验数据
    if form.is_valid():
        form.save()
        return redirect('/super_list/')
    # 校验失败
    return render(request, 'super_add.html', {"form": form})

def super_edit(request, nid):
    """账号编辑"""

    if request.method == "GET":
        # 根据传递的id获取那一行的数据
        row_object = models.SuperNum.objects.filter(id=nid).first()

        form = SuperEditModelForm(instance=row_object)
        return render(request, 'super_edit.html', {'form': form})

    # 保证改变的数据是id=nid的那一行
    row_object = models.SuperNum.objects.filter(id=nid).first()
    form = SuperEditModelForm(data=request.POST, instance=row_object)

    # 校验数据,保存
    if form.is_valid():
        form.save()
        return redirect('/super_list/')

    # 校验失败
    return render(request, 'super_edit.html', {"form": form})

def super_del(request, nid):
    """账号删除"""

    models.SuperNum.objects.filter(id=nid).delete()
    return redirect('/super_list/')

