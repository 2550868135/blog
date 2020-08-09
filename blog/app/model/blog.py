''' @File :blog.py @Author:张宇 @Date :2020/8/5 10:55 @Desc : '''
from django.db import models
from django.contrib.auth.models import User
import shortuuid
from enum import Enum

class TagType(Enum):
    python = 'python'
    java = 'java'
    前端 = 'front'
    后端 = 'back'
    人工智能 = 'ai'

def create_id(self):
    return shortuuid.uuid()

class Tag(models.Model):
    type = models.CharField(max_length=50,null=False,blank=False)
    name = models.CharField(max_length=50,default='')
    @classmethod
    def set_tag(cls,type,name):
        tag = Tag.objects.create(type=type,name=name)
class Article(models.Model):
    article_id = models.CharField(max_length=50,unique=True,null=False,db_index=True)
    title = models.CharField(max_length=200,null=False,blank=False)
    real_content = models.TextField(default='')
    show_content = models.TextField(default='')
    status = models.BooleanField(default=1)
    tag = models.ForeignKey(Tag,related_name='articles',blank=True,null=True,on_delete=models.SET_NULL)
    user = models.ForeignKey(User,related_name='articles',blank=True,null=True,on_delete=models.SET_NULL)
    last_update = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        index_together = ['article_id','title','tag']



class Item(models.Model):
    item_id = models.CharField(max_length=50,unique=True,null=False,db_index=True)
    name = models.CharField(max_length=200,null=False,blank=False,default='无名称')
    introduce = models.TextField(default='')
    file_url = models.CharField(max_length=500,default='')
    status = models.BooleanField(default=1)
    user = models.ForeignKey(User, related_name='items', blank=True, null=True, on_delete=models.SET_NULL)
    last_update = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)

class Comment(models.Model):
    content = models.CharField(max_length=500,default='')
    article = models.ForeignKey(Article,related_name='comments',blank=True, null=True, on_delete=models.SET_NULL)
    author = models.ForeignKey(User,related_name='comments',blank=True, null=True, on_delete=models.SET_NULL)
    create_time = models.DateTimeField(auto_now_add=True)

class Data(models.Model):
    data_id = models.CharField(max_length=50,unique=True,null=False,db_index=True)
    describe = models.TextField(default='')
    file_url = models.CharField(max_length=500, default='')
    user = models.ForeignKey(User, related_name='datas', blank=True, null=True, on_delete=models.SET_NULL)
    last_update = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now_add=True)