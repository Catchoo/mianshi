import logging
import re
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from .form import  FileUploadForm
from utils import celery_tasks


# Create your views here.
# logger = logging.getLogger(__name__)


def index(request):
    return render(request,"send_excel.html")

def upload(request):
    # 判断请求方法是否为post
    if request.is_ajax():
        f_obj = request.FILES.get("f")
        # print(f_obj)
        name = f_obj.name
        print(name)
    # 将文件传递给celery解析
    celery_tasks.upload.delay(f_obj,name)


    return JsonResponse({"result":200})