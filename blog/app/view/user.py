''' @File :user.py @Author:张宇 @Date :2020/8/1 22:58 @Desc : '''
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.shortcuts import render,reverse,redirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from app.libs.common import video_qiniu
from app.model.auth import Setting


class SettingView(View):
    TEMPLATE = 'user/settings.html'

    @method_decorator(login_required)
    def get(self,request):
        user = request.user
        data = {}
        data['user'] = user
        return render(request,self.TEMPLATE,data)

    def post(self,request):
        user_id = request.POST.get('user')
        file = request.FILES.get('file')
        if file:
            result = video_qiniu.put(file.name,file.read())
            if result:
                user = User.objects.get(id=user_id)
                exists = Setting.objects.filter(user=user).exists()
                if not exists:
                    setting = Setting.objects.create(user=user,head_img=result)
                else:
                    setting = Setting.objects.get(id=user.setting.id)
                    setting.head_img = result
                    setting.save()
                return JsonResponse({'code':0,'url':result})
            else:
                return JsonResponse({'code':1})
        return JsonResponse({'code':1})

class UpdateInfo(View):

    def post(self,request):
        nickname = request.POST.get('nickname')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        content = request.POST.get('content')
        user = request.user
        setting = Setting.objects.get(id=user.setting.id)
        setting.updateInfo(nickname,age,gender,phone,email,content)
        setting.save()
        return redirect('settings')
