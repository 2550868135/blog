''' @File :urls.py @Author:张宇 @Date :2020/8/1 14:52 @Desc : '''
from django.urls import path
from app.view.blogs import BlogView,LoginView

urlpatterns = [
                path('',BlogView.as_view(),name='blog'),
                path('login/',LoginView.as_view(),name='login')
]