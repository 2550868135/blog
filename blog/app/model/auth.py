''' @File :auth.py @Author:张宇 @Date :2020/8/2 15:27 @Desc : '''
from django.db import models
from django.contrib.auth.models import User

class Setting(models.Model):
    age = models.IntegerField(default=0)
    nick_name = models.CharField(max_length=50,default='')
    gender = models.CharField(max_length=10,default='')
    head_img = models.CharField(max_length=500,default='https://ss0.bdstatic.com/70cFuHSh_Q1YnxGkpoWK1HF6hhy/it/u=38616266,2952961838&fm=26&gp=0.jpg',db_index=True)
    content = models.TextField(default='该用户很懒,什么也没写!')
    phone = models.CharField(max_length=20)
    email = models.EmailField(default='')
    update_time = models.DateTimeField(auto_now=True)
    user = models.OneToOneField(User,blank=True,null=True,on_delete=models.SET_NULL,related_name='setting')

    def updateInfo(self,nickname,age,gender,phone,email,content):
        self.nick_name = nickname
        self.age = age
        self.gender = gender
        self.phone = phone
        self.email = email
        self.content = content

    def __str__(self):
        return "nickname:{},age:{}".format(self.nick_name,self.age)