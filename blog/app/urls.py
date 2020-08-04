''' @File :urls.py @Author:张宇 @Date :2020/8/1 14:52 @Desc : '''
from django.urls import path
from app.view.blogs import BlogView,LoginView,LogoutView,test
from app.view.user import SettingView,UpdateInfo
from app.view.dashboard import DashboardIndex,ChangeStatus,PicSetting,RemovePic

urlpatterns = [
                path('',BlogView.as_view(),name='blog'),
                path('login/',LoginView.as_view(),name='login'),
                path('logout/',LogoutView.as_view(),name='logout'),
                path('user/settings/',SettingView.as_view(),name='settings'),
                path('dashboard/user',DashboardIndex.as_view(),name='dashboard'),
                path('user/update/',UpdateInfo.as_view(),name='update'),
                path('dashboard/user/change/',ChangeStatus.as_view(),name='change_status'),
                path('dashboard/picture/',PicSetting.as_view(),name='pic_setting'),
                path('dashboard/picture/remove/',RemovePic.as_view(),name='remove_picture'),
                path('test/',test)
]