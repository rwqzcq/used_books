from django.urls import path
from .views import *
app_name = 'book'
urlpatterns = [
    path('', index, name='index'),
    path('list/<int:cid>', book_list, name="list"),
    path('detail/<int:bid>', book_detail, name="detail"), # 图书详情
    path('buy', buy, name="buy"), # 订购
    path('search', search, name='search'), # 搜索
    path('notice_list', notice_list, name="notice_list"), # 公告列表
    path('notice_detail/<int:nid>', notice_detail, name='notice_detail'), # 公告详情
]