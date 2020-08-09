''' @File :blogs.py @Author:张宇 @Date :2020/8/1 14:48 @Desc : '''
from django.views.generic import View
from django.shortcuts import render,reverse,redirect
from django.http import JsonResponse
from django.contrib.auth.models import User
from app.model.dashboard import Picture
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from app.model.blog import Article,Tag,TagType,Item,Comment,Data
import qiniu
from app.utils.get_strftime import get_strftime
import shortuuid


class BlogView(View):
    TEMPLATE = 'blog/blog_index.html'
    @method_decorator(login_required)
    def get(self,request,name='all'):
        page_size = 5
        pics = Picture.objects.all().order_by('index')
        user = request.user
        all_tags = Tag.objects.all()
        if not name:
            total = Article.objects.all().count()
            articles = Article.objects.filter(status=1).all()
        else:
            tag = Tag.objects.filter(name=name)
            if tag:
                tag = tag[0]
                total = Article.objects.filter(status=1, tag_id=tag.id).all().count()
                articles = Article.objects.filter(status=1,tag_id=tag.id).all()
                print(articles)
            else:
                total = Article.objects.all().count()
                articles = Article.objects.filter(status=1).all()
        tags = list(Article.objects.raw("select app_tag.id,app_tag.name as name,app_tag.type as type,count(*) as count from\
         app_article,app_tag where app_article.tag_id=app_tag.id and app_article.status=1 group by app_tag.type"))
        params = {}
        for t in tags:
            params[t.type] = t.count
        total_page = int(total/page_size) if total%page_size==0 else total//page_size + 1
        page = request.GET.get('page', '')
        if not page:
            page = 1
            articles = articles[(page-1):page*page_size]
            data = {'user': user, 'pics': pics, 'params': params, 'articles': articles, 'all_tags': all_tags,'total_page':total_page,'current_tag':name}
            return render(request, self.TEMPLATE, data)
        else:
            page = int(page)
            articles = articles[(page-1)*page_size:page*page_size]
            data = {}
            for article in articles:
                create_time = get_strftime(article.create_time)
                data[article.article_id] = {
                    'title':article.title,
                    'create_time':create_time,
                    'head_img':article.user.setting.head_img,
                    'username':article.user.username,
                    'show_content':article.show_content[:100]
                }
            return JsonResponse({'data':data})


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
            return redirect(reverse('blog',kwargs={'tag':''}))


class LogoutView(View):

    def get(self,request):
        logout(request)
        return redirect(reverse('login'))


class CreateArticle(View):
    @method_decorator(login_required)
    def get(self,request):
        user = request.user
        tags = Tag.objects.all()
        data = {'user':user,'tags':tags}
        return render(request,'blog/article_edit.html',data)

    def post(self,request):
        user_id = int(request.POST.get('user_id'))
        tag = request.POST.get('tag')
        title = request.POST.get('title')
        real_content = request.POST.get('real_content')
        show_content = request.POST.get('show_content')
        user = User.objects.filter(id=user_id)
        tag = Tag.objects.filter(type=tag)
        if user and tag:
            article = Article(article_id=shortuuid.uuid(),title=title,real_content=real_content,show_content=show_content,user=user[0],tag=tag[0])
            article.save()
            return JsonResponse({'code':0,'message':'发表成功'})
        else:
            return JsonResponse({'code':1,'message':'发表失败'})


class AritcleDetail(View):
    TEMPLATE = 'blog/detail_article.html'

    @method_decorator(login_required)
    def get(self,request):
        article_id = request.GET.get('id')
        article = Article.objects.filter(article_id=article_id)
        user = request.user
        comments = Comment.objects.filter(article_id=article[0].id,author_id=user.id)
        if article:
            data = {'article':article[0],'comments':comments}
            return render(request,self.TEMPLATE,data)
        else:
            return redirect(redirect('blog',kwargs={'tag':''}))


class Items(View):
    TEMPLATE = 'blog/items.html'

    @method_decorator(login_required)
    def get(self,request):
        user = request.user
        items = Item.objects.filter(status=1).all()
        data = {'user': user,'items':items}
        return render(request,self.TEMPLATE,data)

    def post(self,request):
        user = request.user
        name = request.POST.get('name')
        introduce = request.POST.get('introduce')
        file_url = request.POST.get('file_url')
        try:
            item = Item.objects.create(item_id=shortuuid.uuid(),name=name,introduce=introduce,file_url=file_url,user=user)
            return JsonResponse({'code':0})
        except :
            return JsonResponse({'code':1,'message':'保存失败!'})


def UploadToken(request):
    access_key = '2zdV4opbmFZaDcTF0yUfW25kymJrpWNpx3MtkUwM'
    secret_key = '2fw3FgmHRaoYdSyUca8A3clQKiowHDiL4FsusSEC'
    q = qiniu.Auth(access_key, secret_key)
    bucket = 'items-dock'
    token = q.upload_token(bucket)
    return JsonResponse({'uptoken':token})

class AddComment(View):
    def post(self,request):
        article_id = request.POST.get('article_id')
        user = request.user
        content = request.POST.get('content')
        if article_id:
            article = Article.objects.filter(article_id=article_id)
            if article:
                article = article[0]
                comment = Comment.objects.create(content=content,article_id=article.id,author_id=user.id)
                return JsonResponse({'code':0})
            else:
                return JsonResponse({'code':1,'message':'找不到文章!'})
        return JsonResponse({'code':1,'message':'请输入文章id!'})

class Datas(View):
    TEMPLATE = 'blog/datas.html'

    @method_decorator(login_required)
    def get(self, request):
        user = request.user
        datas = Data.objects.all()
        data = {'user': user, 'datas': datas}
        return render(request, self.TEMPLATE, data)

    def post(self, request):
        user = request.user
        describe = request.POST.get('describe')
        file_url = request.POST.get('file_url')
        try:
            data = Data.objects.create(data_id=shortuuid.uuid(), describe=describe, file_url=file_url,
                                       user=user)
            return JsonResponse({'code': 0})
        except:
            return JsonResponse({'code': 1, 'message': '保存失败!'})