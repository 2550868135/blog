''' @File :blogs.py @Author:张宇 @Date :2020/8/1 14:48 @Desc : '''
from django.views.generic import View
from django.shortcuts import render,reverse,redirect
from django.contrib.auth.models import User
from app.model.dashboard import Picture
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class BlogView(View):
    TEMPLATE = 'blog/blog_index.html'
    @method_decorator(login_required)
    def get(self,request):
        pics = Picture.objects.all().order_by('index')
        user = request.user
        data = {'user':user,'pics':pics}
        return render(request,self.TEMPLATE,data)


class LoginView(View):
    TEMPLATE = 'blog/login.html'
    def get(self,request):
        if request.user.is_authenticated:
            return redirect(reverse('blog'))
        next = request.GET.get('next','')
        data = {'next':next}
        return render(request,self.TEMPLATE,data)

    def post(self,request):
        username = request.POST.get('username')
        password = request.POST.get('password')
        next = request.POST.get('next')

        data = {}
        if not all([username,password]):
            data['error'] = '用户名或密码不能为空!'
            return render(request,self.TEMPLATE,data)

        user = User.objects.filter(username=username)
        if user[0].is_active == 0:
            data['error'] = '用户已被禁用,请联系管理员!'
            return render(request, self.TEMPLATE, data)

        user = User.objects.filter(username=username)
        if not user:
            data['error'] = '用户名错误!'
            return render(request, self.TEMPLATE, data)

        user = authenticate(username=username,password=password)
        if not user:
            data['error'] = '密码错误!'
            return render(request, self.TEMPLATE, data)

        #登录
        login(request,user)
        if next:
            return redirect(next)
        else:
            return redirect(reverse('blog'))


class LogoutView(View):

    def get(self,request):
        logout(request)
        return redirect(reverse('login'))


def test(request):
    return render(request,'blog/article_edit.html')