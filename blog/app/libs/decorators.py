''' @File :decorators.py @Author:张宇 @Date :2020/8/2 16:42 @Desc : '''

from functools import wraps
from django.shortcuts import redirect,reverse

def is_super(func):
    @wraps(func)
    def check(self,request,*args,**kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            return func(self,request,*args,**kwargs)
        else:
            return redirect(reverse('blog'))
    return check
