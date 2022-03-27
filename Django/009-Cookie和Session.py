# -*- coding = utf-8 -*-
# @Time : 2022/3/13 21:30
# @Author : spray_dream
# @File : 009-Cookie和Session.py
# @Software: PyCharm
pass
"""
http请求是无状态的短链接,无状态是指每次发送请求和响应都是新的,不携带上一次请求时的信息,例如用户的登录状态.
用Cookie和Session可以解决
在用户发送完请求后,网站响应时,除了携带响应体即HTML之外,还有响应头:cookie,cookie可以理解为字典,键值对,一个凭证
这样下次再访问网站时会把它携带过去,是能通过某些需要登陆的页面的凭证
这个cookie也会被存储在一个空间里(session:数据库,redis,文件)
当有带着cookie的url访问时,会将这个键值对和session里的cookie比对,如果存在就会允许访问
"""

"""
当用MySQL删除了某张表后,把所有有关这张表的代码全给注释掉,再执行迁移文件,和python manage.py migrate --fake
然后恢复注释的代码,执行迁移文件和迁移
"""
