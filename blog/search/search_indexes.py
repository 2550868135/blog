''' @File :search_indexes.py @Author:张宇 @Date :2020/10/2 14:34 @Desc : '''
import datetime
from haystack import indexes
from app.model.blog import Data,Item,Article


class ArticleIndex(indexes.SearchIndex, indexes.Indexable):
    """对文章模型类部分字段建立索引,索引最后会存储在ES索引库中"""
    #use_template=true表示把结果保存到模板中,需要在templates文件夹下新建文件,对应template_name
    text = indexes.CharField(document=True, use_template=True,template_name='search/articles_text.txt')

    def get_model(self):
        #指索引哪个模型类
        return Article

    def index_queryset(self, using=None):
        """当Article模型类中的索引有更新时调用"""
        #只更新指定筛选条件的索引
        return self.get_model().objects.filter(last_update__lte=datetime.datetime.now())


class ItemIndex(indexes.SearchIndex, indexes.Indexable):
    """对项目模型类部分字段建立索引,索引最后会存储在ES索引库中"""
    text = indexes.CharField(document=True, use_template=True,template_name='search/items_text.txt')

    def get_model(self):
        #指索引哪个模型类
        return Item

    def index_queryset(self, using=None):
        #只更新指定筛选条件的索引
        return self.get_model().objects.filter(last_update__lte=datetime.datetime.now())

class DataIndex(indexes.SearchIndex, indexes.Indexable):
    """对资源模型类部分字段建立索引,索引最后会存储在ES索引库中"""
    text = indexes.CharField(document=True, use_template=True,template_name='search/datas_text.txt')

    def get_model(self):
        #指索引哪个模型类
        return Data

    def index_queryset(self, using=None):
        #只更新指定筛选条件的索引
        return self.get_model().objects.filter(last_update__lte=datetime.datetime.now())