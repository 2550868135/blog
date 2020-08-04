''' @File :dashboard.py @Author:张宇 @Date :2020/8/3 15:59 @Desc : '''

from django.db import models

class Picture(models.Model):
    image = models.CharField(max_length=500)
    index = models.IntegerField(db_index=True,unique=True)
