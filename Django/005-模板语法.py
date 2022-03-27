# -*- coding = utf-8 -*-
# @Time : 2022/3/5 20:55
# @Author : spray_dream
# @File : 005-模板语法.py
# @Software: PyCharm
pass
"""
本质上:在HTML中写一些占位符,由数据对这些占位符进行替换和处理
"""

"""
1.要想将自己数据返回到网页上,需要以字典的形式:
def tpl(request):
    name = 'spray'
    roles = ["管理员", "CEO", "保安"]
    # 可以填写获取到的数据
    return render(request, 'tpl.html', {"n1": name, "n2": roles})
然后在HTML页面上写上字典的键(随便写),并且大括号表示:{{ n1 }},在HTML中取索引只能用n.0或n.1或n.2
2.前端接收后端数据并进行处理即模板语法共有两种分别是{{  }}和{%  %}，
    django模板语法的取值是固定格式，只能采用.进行取值，既可以.索引也可以点.key
    {{  }}    # 变量相关，用在接收后端传递过来的数据、过滤器、自定义过滤器
    {% %}     # 逻辑相关，用在标签(if判断 for循环)、自定义标签simple_tag、inclusion_tag、模版继承extend和导入include
    <p>{{ d.key }}</p>            # 字典使用点key方式
    <p>{{ my_str.0 }}</p>         # 字符串使用点索引的方式
    <p>{{ l.0 }}</p>              # 列表使用点索引的方式
    <p>{{ obj.get_class }}</p>    # 对象点属性或方法的方式
3.过滤器
过滤器filters
在Django的模板语言中，可以通过过滤器改变变量的显示，过滤器就类似于是模版语法内置的内置方法，与后端数据类型的内置方法类似，
基本语法为{{数据|过滤器:参数}}，其中参数是可选的，两个参数分别在管道符|前后，但是过滤器最多只能有两个参数，
过滤器支持链式操作，即一个过滤器的输出可以作为另一个过滤器的输入，django中内置了60多种过滤器，这里介绍一些常用的过滤器。
<!--常用过滤器-->
<p>统计长度{{ my_str|length }}</p>
<p>默认值，如果布尔值是True,默认值就是True,否则展示冒号后面的值{{ my_bool|default:'啥也不是' }}</p>
<p>文件大小：{{ file_size|filesizeformat }}</p>
<p>日期格式化：{{ current_time|date:'Y-m-d H:i:s' }}</p>
<p>切片操作，支持步长，顾头不顾尾{{ my_list|slice:'0:2:1' }}</p>
<p>摘要操作包含三个点（比如掘金文章的摘要）{{ info|truncatechars:9 }}</p>
<p>切取单词,不包含三个点，只会按照空格切分单词{{ egn|truncatewords:'9' }}</p>
<p>移除特定的字符{{ msg|cut:' ' }}</p>
<p>拼接操作{{ my_str|join:'@' }}</p>
<p>加法运算（拼接操作）{{ my_int|add:12 }}</p>
<p>加法运算（拼接操作）{{ my_str|add:'12' }}</p>
4.在后端写前端代码
    (1)safe过滤器
    <!--后端代码-->
    def index(request):
        h = '<h1>我是html标签</h1>'
        return render(request, 'render_html.html', locals())
    <!-- 前端转义,过滤器的意思是告诉浏览器后端写的标签是安全的，可以进行渲染 -->
    {{h|safe}}
    (2)通过模板语法
    <!--后端代码-->
    from django.utils.safestring import mark_safe
    def index(request):
        s = '<h1>后端转义</h1>'
        res = mark_safe(s)
        return(request, 'render_html.html', locals())
    <!--前端代码-->
    {{res}}
5.for循环:
在前端页面使用模板语言对数据进行for循环时，有两种用法，一种是像python一样直接循环输出被for循环对象中的每个元素，
另一种是通过forloop得到每个元素的信息。for循环的模板语法如下：
    {% for i in variable %}
        variable非空时执行的代码
        {% empty %}
            variable为空时执行的代码
    {% endfor %}
</body>

6.with起别名
在with语法内可以通过as后面的别名快速的使用到前面非常复杂的获取数据的方式所得到的的数据，即给复杂的变量起别名，比如：
def index(request):
    my_dic = {
        'name': 'python',
        'age': 18,
        'hobby': ['study', 'play']
    }
    return render(request, 'render_html.html', locals())

{% with my_dic.hobby.0 as myhobby %}
    with语法{{ myhobby }}
    直接获取{{ my_dic.hobby.0 }}
{% endwith %}
"""
