"""
步骤:定义中间件,在settings中注册中间件
"""

'''
from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse

# 1342
class M1(MiddlewareMixin):
    """中间件1"""

    def process_request(self, request):
        print(1)
        # 没有返回值(None),可以继续往后走
        # return HttpResponse("无权访问")    # 如果有返回值,返回值和视图函数里的差不多 12

    def process_response(self, request, response):
        print(2)
        return response


class M2(MiddlewareMixin):
    """中间件2"""

    def process_request(self, request):
        print(3)

    def process_response(self, request, response):
        print(4)
        return response
'''

from django.utils.deprecation import MiddlewareMixin
from django.shortcuts import HttpResponse, redirect

class AuthMiddleware(MiddlewareMixin):

    def process_request(self, request):

        # 首先一定要排除不需要cookie信息的页面
        if request.path_info in ["/login/", "/image_code/"]:
            return

        # 1.读取当前访问的用户的session信息,如果能读到,说明已登录,可以继续往后走
        info_dict = request.session.get("info")
        # 2.有登录信息,进行下一步
        if info_dict:
            return
        # 3.没有登录,重定向到登录页面
        return redirect('/login/')

    # def process_response(self, request, response):
    #     return response
