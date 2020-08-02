''' @File :dashboard.py @Author:张宇 @Date :2020/8/2 16:40 @Desc : '''
# 后台管理页面
from django.views.generic import View
from django.shortcuts import render,reverse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from app.libs.decorators import is_super

class DashboardIndex(View):

    TAMPLATE = 'dashboard/dashboard_index.html'
    @is_super
    def get(self,request):
        users = User.objects.all()
        data = {'users':users}
        return render(request,self.TAMPLATE,data)