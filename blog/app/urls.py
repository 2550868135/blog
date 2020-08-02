''' @File :urls.py @Author:张宇 @Date :2020/8/1 14:52 @Desc : '''
from django.urls import path
from app.view.blogs import BlogView,LoginView,LogoutView
from app.view.user import SettingView,UpdateInfo
from app.view.dashboard import DashboardIndex

urlpatterns = [
                path('',BlogView.as_view(),name='blog'),
                path('login/',LoginView.as_view(),name='login'),
                path('logout/',LogoutView.as_view(),name='logout'),
                path('user/settings/',SettingView.as_view(),name='settings'),
                path('dashboard/',DashboardIndex.as_view(),name='dashboard'),
                path('user/update/',UpdateInfo.as_view(),name='update')
]