''' @File :user.py @Author:张宇 @Date :2020/8/1 22:58 @Desc : '''
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import View
from django.shortcuts import render, reverse, redirect
from django.contrib.auth.models import User
from django.http import JsonResponse
from app.libs.common import video_qiniu
from app.model.auth import Setting
from app.model.blog import Article, Tag,Item,Data


class SettingView(View):
    TEMPLATE = 'user/settings.html'

    @method_decorator(login_required)
    def get(self, request):
        user = request.user
        data = {}
        data['user'] = user
        code = request.GET.get('code')
        data['code'] = code
        return render(request, self.TEMPLATE, data)

    def post(self, request):
        user_id = request.POST.get('user')
        file = request.FILES.get('file')
        if file:
            result = video_qiniu.put(file.name, file.read())
            if result:
                user = User.objects.get(id=user_id)
                exists = Setting.objects.filter(user=user).exists()
                if not exists:
                    setting = Setting.objects.create(user=user, head_img=result)
                else:
                    setting = Setting.objects.get(id=user.setting.id)
                    setting.head_img = result
                    setting.save()
                return JsonResponse({'code': 0, 'url': result})
            else:
                return JsonResponse({'code': 1})
        return JsonResponse({'code': 1})


class UpdateInfo(View):

    def post(self, request):
        nickname = request.POST.get('nickname')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        content = request.POST.get('content')
        user = request.user
        setting = Setting.objects.get(id=user.setting.id)
        setting.updateInfo(nickname, age, gender, phone, email, content)
        setting.save()
        return redirect('{}?code=0'.format(reverse('settings')))


class MyArticle(View):
    TEMPLATE = 'user/my_article.html'

    @method_decorator(login_required)
    def get(self, request):
        user = request.user
        data = {'user': user}
        try:
            articles = Article.objects.filter(user_id=user.id)
            if articles:
                data['articles'] = articles
        except:
            pass
        return render(request, self.TEMPLATE, data)

class UpdateBlog(View):
    TEMPLATE = 'user/update_blog.html'

    @method_decorator(login_required)
    def get(self, request):
        user = request.user
        data = {'user': user}
        article_id = request.GET.get('article_id')
        article = Article.objects.filter(article_id=article_id)
        if article:
            data['article'] = article[0]
            tags = Tag.objects.all()
            data['tags'] = tags
            return render(request,self.TEMPLATE,data)

        return redirect(reverse('my_article'))

    def post(self,request):
        user_id = request.POST.get('user_id')
        type = request.POST.get('tag')
        title = request.POST.get('title')
        real_content = request.POST.get('real_content')
        show_content = request.POST.get('show_content')
        article_id = request.POST.get('article_id')
        tag = Tag.objects.filter(type=type)
        article = Article.objects.filter(article_id=article_id,user_id=user_id)
        if tag and article:
            article = article[0]
            article.tag = tag[0]
            article.title = title
            article.real_content = real_content
            article.show_content = show_content
            article.save()
            return JsonResponse({'code':0,'message':'修改成功!'})
        else:
            return JsonResponse({'code':1,'message':'修改失败!'})

class DeleteBlog(View):
    TEMPLATE = 'user/my_article.html'

    @method_decorator(login_required)
    def get(self,request):
        user = request.user
        article_id = request.GET.get('article_id','')
        data = {}
        if article_id:
            data['refresh'] = 1
            article = Article.objects.filter(user=user,article_id=article_id)
            if article:
                article.delete()
            else:
                data['error'] = '删除失败'
        data['user'] = user
        try:
            articles = Article.objects.filter(user_id=user.id)
            if articles:
                data['articles'] = articles
        except:
            pass
        return render(request,self.TEMPLATE,data)

class MyItem(View):
    TEMPLATE = 'user/my_item.html'

    @method_decorator(login_required)
    def get(self,request):
        user = request.user
        items = Item.objects.filter(user_id=user.id).all()
        data = {'user':user,'items':items}
        return render(request,self.TEMPLATE,data)


class DeleteItem(View):

    @method_decorator(login_required)
    def get(self,request):
        user = request.user
        item_id = request.GET.get('item_id')
        data = {}
        if item_id:
            item = Item.objects.filter(user=user,item_id=item_id)
            if item:
                item.delete()
                return JsonResponse({'code':0})
            else:
                return JsonResponse({'code':1,'message':'删除失败!'})
        return JsonResponse({'code':1,'message':'找不到该项目!'})

class UpdateItem(View):

    def post(self,request):
        user = request.user
        name = request.POST.get('name')
        introduce = request.POST.get('introduce')
        file_url = request.POST.get('file_url')
        item_id = request.POST.get('item_id')
        try:
            if item_id:
                item = Item.objects.filter(item_id=item_id)
                if item:
                    item=item[0]
                    item.name=name
                    item.introduce=introduce
                    item.file_url=file_url
                    item.save()
                    return JsonResponse({'code':0})
                else:
                    return JsonResponse({'code': 1, 'message': '找不到该项目!'})
            else:
                return JsonResponse({'code':1,'message':'找不到项目id!'})
        except :
            return JsonResponse({'code':1,'message':'更新失败!'})


class MyData(View):
    TEMPLATE = 'user/my_data.html'

    @method_decorator(login_required)
    def get(self,request):
        user = request.user
        datas = Data.objects.filter(user_id=user.id).all()
        data = {'user':user,'datas':datas}
        return render(request,self.TEMPLATE,data)


class DeleteData(View):

    @method_decorator(login_required)
    def get(self, request):
        user = request.user
        data_id = request.GET.get('data_id')
        data = {}
        if data_id:
            data_ = Data.objects.filter(user=user,data_id=data_id)
            if data_:
                data_.delete()
                return JsonResponse({'code': 0})
            else:
                return JsonResponse({'code': 1, 'message': '删除失败!'})
        return JsonResponse({'code': 1, 'message': '找不到该资料!'})


class UpdateData(View):

    def post(self, request):
        user = request.user
        describe = request.POST.get('describe')
        file_url = request.POST.get('file_url')
        data_id = request.POST.get('data_id')
        try:
            if data_id:
                data = Data.objects.filter(data_id=data_id)
                if data:
                    item = data[0]
                    item.describe = describe
                    item.file_url = file_url
                    item.save()
                    return JsonResponse({'code': 0})
                else:
                    return JsonResponse({'code': 1, 'message': '找不到该资料!'})
            else:
                return JsonResponse({'code': 1, 'message': '找不到资料id!'})
        except:
            return JsonResponse({'code': 1, 'message': '更新失败!'})
