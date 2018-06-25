import logging

from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from .form import  FileUploadForm



# Create your views here.
# logger = logging.getLogger(__name__)


def index(request):
    return render(request,"send_excel.html")

def upload(request):
    # 判断请求方法是否为postq
    print(2223234342)
    print(request.method)
    if request.is_ajax():
        f_obj = request.FILES.get("f")
        print(f_obj)
        name = f_obj.name
        print(name)
        f_write = open(name, "wb")
        for line in f_obj:
            f_write.write(line)
        return HttpResponse("上传成功")
    # return render(request, 'send_excel.html')
    # 判断是否为excel文件格式

    # 将文件存储到当前项目目录下

    # 将文件传递给celery解析
    pass

