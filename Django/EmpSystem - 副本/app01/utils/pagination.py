# -*- coding = utf-8 -*-
# @Time : 2022/3/12 20:51
# @Author : spray_dream
# @File : pagination.py
# @Software: PyCharm

"""
分页组件
使用方法:在视图函数中
# 1.根据情况筛选数据
queryset = models.SuperNum.objects.filter(**data_dict).all()
# 2.实例化分页的类
page_object = Pagination(request, queryset)
# 3.分页之后的数据
page_queryset = page_object.page_queryset    # 每页展示的数据,之后可以在前端做循环展示
page_string = page_object.html()    # 分页的页码图层
context = {"queryset": page_queryset, "value": value, "page_string": page_string}
return render(request, 'super_list.html', context)
在前端页面中:
{% for i in queryset %}
<tr>
    <td>{{ i.~~~ }}</td>
    <td>{{ i.~~~ }}</td>
    <td>{{ i.~~~ }}</td>
</tr>
{% endfor %}

# 页码图层
<ul class="pagination">
    {{ page_string }}
</ul>
"""
from django.utils.safestring import mark_safe


class Pagination:

    def __init__(self, request, queryset, page_param="page_param", page_size=10, plus=5):
        """
        request:请求的对象
        queryset:符合条件的数据
        page_size:每页显示多少行
        page_param:url传递的要跳转的页面,?page=1
        plus:当前页码的前后plus页
        """
        from django.http.request import QueryDict
        import copy
        query_dict = copy.deepcopy(request.GET)
        query_dict._mutable = True
        self.query_dict = query_dict

        self.page_param = page_param
        page = request.GET.get(page_param, "1")

        # 如果输入的不是十进制的数,就显示第1页
        if page.isdecimal():
            page = int(page)
        else:
            page = 1
        self.page = page
        self.page_size = page_size
        self.start = (page - 1) * page_size
        self.end = page * page_size
        self.page_queryset = queryset[self.start: self.end]

        total_count = queryset.count()
        total_page, div = divmod(total_count, self.page_size)
        # 总条数%每页展示多少条数据,余数不为0时页码向上取整
        if div:
            total_page += 1
        self.total_page = total_page
        self.plus = plus

    def html(self):
        # 计算并显示当前页码的前5个和后5个
        # 当页码数较少时,直接展示前11个
        if self.total_page <= 2 * self.plus + 1:
            start_page = 1
            end_page = self.total_page

        # 当数据库中数据较多时,大于11
        else:
            # 当前页码<=5时,页码从1开始
            if self.page <= self.plus:
                start_page = 1
                end_page = 2 * self.plus + 1

            # 页码大于5时,直接显示前5个和后5个
            else:
                # 当前页码+plus>总页码时,需要限制极值
                if (self.page + self.plus) > self.total_page:
                    start_page = 1
                    end_page = self.total_page
                else:
                    start_page = self.page - self.plus
                    end_page = self.page + self.plus

        # 页码
        page_str_list = []

        self.query_dict.setlist(self.page_param, [1])
        print(self.query_dict.urlencode())
        # 首页
        page_str_list.append('<li><a href="?{}">首页</a></li>'.format(self.query_dict.urlencode()))
        # 上一页
        if self.page > 1:
            self.query_dict.setlist(self.page_param, [self.page - 1])
            prev = '<li><a href="?{}">上一页</a></li>'.format(self.query_dict.urlencode())
        # 限制页码是1时上一页的链接
        else:
            self.query_dict.setlist(self.page_param, [1])
            prev = '<li><a href="?{}">上一页</a></li>'.format(self.query_dict.urlencode())
        # 将上一页的标签和链接添加到页码图层最左边
        page_str_list.append(prev)

        # 当前列表页面显示的页码
        for i in range(start_page, end_page + 1):
            self.query_dict.setlist(self.page_param, [i])
            if i == self.page:
                # 突出当前页码
                ele = '<li class="active"><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            else:
                ele = '<li><a href="?{}">{}</a></li>'.format(self.query_dict.urlencode(), i)
            page_str_list.append(ele)

        # 下一页
        if self.page < self.total_page:
            self.query_dict.setlist(self.page_param, [self.page + 1])
            prev = '<li><a href="?{}">下一页</a></li>'.format(self.query_dict.urlencode())
        # 限制页码是total_page时下一页的链接
        else:
            self.query_dict.setlist(self.page_param, [self.total_page])
            prev = '<li><a href="?{}">下一页</a></li>'.format(self.query_dict.urlencode())
        # 将上一页的标签和链接添加到页码图层最右边
        page_str_list.append(prev)
        # 尾页
        self.query_dict.setlist(self.page_param, [self.total_page])
        page_str_list.append('<li><a href="?{}">尾页</a></li>'.format(self.query_dict.urlencode()))

        # 输入跳转页码
        searching_string = """
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
           """
        page_str_list.append(searching_string)

        # 将页码图层添加到html中
        page_string = mark_safe("".join(page_str_list))
        return page_string
