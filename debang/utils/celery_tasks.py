from celery import Celery

# 创建celery对象,通过broker制定redis为存储队列
app = Celery("celery_task",broker='redis://127.0.0.1:6379/1')

