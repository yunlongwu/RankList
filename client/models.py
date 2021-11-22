from django.db import models


# Create your models here.

class Client(models.Model):
    """
    客户端信息
    """
    client_id = models.CharField(max_length=20, unique=True, verbose_name="客户端编号")
    points = models.IntegerField(default=1, verbose_name="分数")

    class Meta:
        ordering = ['-points', '-id']
