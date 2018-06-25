from celery import Celery

# 创建celery对象,通过broker制定redis为存储队列
app = Celery("celery_task",broker='redis://127.0.0.1:6379/1')
@app.task
def upload(request,f_obj,name):

    # 判断是否为excel文件格式
    try:
        res = re.match(r"^\.*\.excel$",name).group()
        if res:
            # 将文件存储到当前项目目录下
            f_write = open(name, "wb")
            for line in f_obj:
                f_write.write(line)

    except:
        return JsonResponse({"result":909})



