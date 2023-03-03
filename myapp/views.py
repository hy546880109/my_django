from django.shortcuts import render
from django.http import HttpResponse
import json
from . import models


# Create your views here.
def login(request):
    if request.method == "GET":
        result = {}  # 先指定一个字典
        name = models.Name.objects.get(pk=1).user
        sex = models.Name.objects.get(pk=1).sex
        age = models.Name.objects.get(pk=1).age
        result['name'] = name
        result['sex'] = sex
        result['age'] = age
        result = json.dumps(result)
        # 指定返回数据类型为json且编码为utf-8
        return HttpResponse(result, content_type='application/json;charset=utf-8')

