import logging
from django.db import models
import uuid
logger = logging.getLogger(__name__)


# Create your models here.


class People(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4(), editable=False)
    NAME = models.CharField(max_length=30, verbose_name="姓名")
    ID = models.BigIntegerField(unique=True, max_length=50, null=False, verbose_name="工号")
    Group = models.ManyToManyField("Orgnz", verbose_name="组织")
    class Meta:
        indexes = [
            models.Index(
                fields=['ID'],
                name='ID_idx',
            )
        ]


class Orgnz(models.Model):
    name = models.CharField(unique=True, max_length=50)
    # people = models.ManyToManyField(People,verbose_name="员工")
    type_choice = (
        ("1", "开发"),
        ("2", "运维"),
        ("3", "产品"),
        ("4", "测试")
    )
    type = models.CharField(choices=type_choice,max_length=4)

    class Meta:
        indexes = [
            models.Index(
                fields=['name'],
                name='name_idx',
            )
        ]