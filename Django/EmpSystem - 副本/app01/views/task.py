import json
from django.shortcuts import render, HttpResponse, redirect
from django.http import JsonResponse
from app01.utils.bootstrap import BootStrapModelForm
from app01 import models
from django import forms
from django.forms.utils import ErrorDict

# 免除ajax的csrf_token认证,以便发送post请求
from django.views.decorators.csrf import csrf_exempt


class TaskModelForm(BootStrapModelForm):
    class Meta:
        model = models.Task
        fields = "__all__"
        widgets = {
            # "detail": forms.Textarea
            "detail": forms.TextInput
        }


def task_list(request):
    # request.GET
    form = TaskModelForm
    return render(request, 'task_list.html', {"form": form})

@csrf_exempt
def task_ajax(request):
    # print(request.GET)    # <QueryDict: {'n1': ['123'], 'n2': ['456']}>

    data_dict = {"status": True, 'data': [11, 22]}
    json_string = json.dumps(data_dict)
    return HttpResponse(json_string)

    # return JsonResponse(data_dict)

@ csrf_exempt
def task_add(request):

    # 用户发送过来的请求用ModelForm校验
    form = TaskModelForm(data=request.POST)
    if form.is_valid():
        form.save()
        data_dict = {"status", True}
        return HttpResponse(json.dumps(data_dict))

    data_dict = {"status": False, 'error': form.errors}
    return HttpResponse(json.dumps(data_dict, ensure_ascii=False))
