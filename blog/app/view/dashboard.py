''' @File :dashboard.py @Author:张宇 @Date :2020/8/2 16:40 @Desc : '''
# 后台管理页面
from django.views.generic import View
from django.shortcuts import render,reverse,redirect
from django.contrib.auth.models import User
from app.model.dashboard import Picture
from app.libs.decorators import is_super
from django.http import JsonResponse
from app.libs.common import video_qiniu
from app.model.blog import Article,Tag,Item,Data

class DashboardIndex(View):

    TAMPLATE = 'dashboard/dashboard_index.html'
    @is_super
    def get(self,request):
        users = User.objects.all()
        data = {'users':users}
        current_user = request.user
        data['current_user'] = current_user
        return render(request,self.TAMPLATE,data)

class ChangeStatus(View):

    @is_super
    def get(self,request):
        try:
            user = request.user
            user.is_active = not user.is_active
            user.save()
            return JsonResponse({'code': 0})
        except :
            return JsonResponse({'code': 1,'message':'修改失败!'})


class PicSetting(View):

    TEMPLATE = 'dashboard/picture_setting.html'

    @is_super
    def get(self,request):
        pics = Picture.objects.all().order_by('index')
        data = {}
        data['pics'] = pics
        data['user'] = request.user
        return render(request,self.TEMPLATE,data)

    def post(self,request):
        file = request.FILES.get('file')
        index = int(request.POST.get('index'))
        if file:
            result = video_qiniu.put(file.name,file.read())
            if result:
                print(result)
                exists = Picture.objects.filter(index=index)
                if not exists:
                    img = Picture.objects.create(index=index,image=result)
                else:
                    img = Picture.objects.get(index=index)
                    img.image = result
                    img.save()
                return JsonResponse({'code':0,'image':result})
            else:
                return JsonResponse({'code':1})
        return JsonResponse({'code':1})

class RemovePic(View):

    @is_super
    def get(self,request):
        index = int(request.GET.get('index'))
        if index:
            try:
                pic = Picture.objects.filter(index=index)
                if pic:
                    pic.delete()
                    return JsonResponse({'code':0})
                else:
                    return JsonResponse({'code':1,'message':'图片不存在'})
            except :
                return JsonResponse({'code':1,'message':'删除失败'})

        return redirect(reverse('pic_setting'))

class ArticleManage(View):
    TEMPLATE = 'dashboard/dashboard_article.html'

    @is_super
    def get(self,request):
        user = request.user
        articles = Article.objects.all()
        data = {'user':user,'articles':articles}
        return render(request,self.TEMPLATE,data)

class ChangeBlogStatus(View):
    TEMPLATE = 'dashboard/dashboard_article.html'
    @is_super
    def get(self,request):
        article_id = request.GET.get('article_id','')
        print(article_id)
        data = {}
        if article_id:
            data['refresh'] = 1
            article = Article.objects.filter(article_id=article_id)
            if article:
                article = article[0]
                article.status = not article.status
                article.save()
            else:
                data['error'] = '修改失败!'
        articles = Article.objects.all()
        data['articles'] = articles
        data['user'] = request.user

        return render(request,self.TEMPLATE,data)

class DeleteDashboardArticle(View):
    TEMPLATE = 'dashboard/dashboard_article.html'

    @is_super
    def get(self, request):
        user = request.user
        article_id = request.GET.get('article_id')
        data = {}
        if article_id:
            data['refresh'] = 1
            article = Article.objects.filter(user=user, article_id=article_id)
            if article:
                article.delete()
            else:
                data['error'] = '删除失败'
        data['user'] = user
        try:
            articles = Article.objects.all()
            if articles:
                data['articles'] = articles
        except:
            pass
        return render(request, self.TEMPLATE, data)

class ItemManage(View):
    TEMPLATE = 'dashboard/dashboard_item.html'

    @is_super
    def get(self,request):
        user = request.user
        items = Item.objects.all()
        data = {'items':items,'user':user}
        return render(request,self.TEMPLATE,data)

class DeleteDashboardItem(View):

    @is_super
    def get(self, request):
        item_id = request.GET.get('item_id')
        if item_id:
            item = Item.objects.filter(item_id=item_id)
            if item:
                item.delete()
                return JsonResponse({'code':0})
            else:
                return JsonResponse({'code':1,'message':'项目不存在!'})
        else:
            return JsonResponse({'code':1,'message':'错误的项目id!'})

class DataManage(View):
    TEMPLATE = 'dashboard/dashboard_data.html'

    @is_super
    def get(self,request):
        user = request.user
        datas = Data.objects.all()
        data = {'datas':datas,'user':user}
        return render(request,self.TEMPLATE,data)

class DeleteDashboardData(View):

    @is_super
    def get(self, request):
        data_id = request.GET.get('data_id')
        if data_id:
            data = Data.objects.filter(data_id=data_id)
            if data:
                data.delete()
                return JsonResponse({'code':0})
            else:
                return JsonResponse({'code':1,'message':'资料不存在!'})
        else:
            return JsonResponse({'code':1,'message':'错误的资料id!'})