''' @File :urls.py @Author:张宇 @Date :2020/8/1 14:52 @Desc : '''
from django.urls import path
from app.view.blogs import BlogView,LoginView,LogoutView,CreateArticle,AritcleDetail,Items,UploadToken,AddComment,Datas
from app.view.user import SettingView,UpdateInfo,MyArticle,UpdateBlog,DeleteBlog,MyItem,DeleteItem,UpdateItem,MyData,DeleteData,UpdateData
from app.view.dashboard import DashboardIndex,ChangeStatus,PicSetting,RemovePic,ArticleManage,ChangeBlogStatus,DeleteDashboardArticle,ItemManage,DeleteDashboardItem,DataManage,DeleteDashboardData
from app.view.message import Message_list,Message_Single,PostMessage,mark_as_read
urlpatterns = [
                path('index/<str:name>/',BlogView.as_view(),name='blog'),
                path('login/',LoginView.as_view(),name='login'),
                path('logout/',LogoutView.as_view(),name='logout'),
                path('user/settings/',SettingView.as_view(),name='settings'),
                path('dashboard/user',DashboardIndex.as_view(),name='dashboard'),
                path('user/update/',UpdateInfo.as_view(),name='update'),
                path('dashboard/user/change/',ChangeStatus.as_view(),name='change_status'),
                path('dashboard/picture/',PicSetting.as_view(),name='pic_setting'),
                path('dashboard/picture/remove/',RemovePic.as_view(),name='remove_picture'),
                path('create/',CreateArticle.as_view(),name='create_article'),
                path('detail/',AritcleDetail.as_view(),name='detail'),
                path('myarticle/',MyArticle.as_view(),name='my_article'),
                path('myarticle/updateblog/',UpdateBlog.as_view(),name='update_blog'),
                path('myarticle/deleteblog',DeleteBlog.as_view(),name='delete_blog'),
                path('dashboard/article/',ArticleManage.as_view(),name='article_manage'),
                path('dashboard/article/change_status',ChangeBlogStatus.as_view(),name='change_blog_status'),
                path('dashboard/article/delete_blog',DeleteDashboardArticle.as_view(),name='delete_dashborad_blog'),
                path('items/',Items.as_view(),name='items'),
                path('uptoken/',UploadToken,name='uptoken'),
                path('myitem/',MyItem.as_view(),name='my_item'),
                path('myitem/deleteitem/',DeleteItem.as_view(),name='delete_item'),
                path('myitem/updateitem/',UpdateItem.as_view(),name='update_item'),
                path('dashboard/item/',ItemManage.as_view(),name='item_manage'),
                path('dashboard/item/delete/',DeleteDashboardItem.as_view(),name='dashboard_item_delete'),
                path('detail/addcomment/',AddComment.as_view(),name='add_comment'),
                path('datas/',Datas.as_view(),name='datas'),
                path('dashboard/data/',DataManage.as_view(),name='data_manage'),
                path('dashboard/data/delete/',DeleteDashboardData.as_view(),name='dashboard_data_delete'),
                path('mydata/',MyData.as_view(),name='my_data'),
                path('mydata/deletedata/',DeleteData.as_view(),name='delete_data'),
                path('mydata/updatedata/',UpdateData.as_view(),name='update_data'),
                path('message/',Message_list.as_view(),name='message_list'),
                path('message/sendmessage/',PostMessage.as_view(),name='post_message'),
                path('message/mark/',mark_as_read,name='mark_as_read'),
                path('message/<str:username>/',Message_Single.as_view(),name='single_message'),

]