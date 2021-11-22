from django.urls import re_path
from client import views

urlpatterns = [
    # 客户端url
]
urlpatterns += [
    # 创建客户端
    re_path('^create_client$', views.create_client),
    # 更新分数
    re_path('^update_point$', views.update_point),
    # 查询排名
    re_path('^query_rank_list$', views.query_rank_list),
]
