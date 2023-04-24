from django.urls import path
from . import views    #从当前模块引入views

app_name = 'zhaosheng'  #设置应用名

urlpatterns = [   
    path('news/<str:newName>/', views.news, name='news'),#新闻列表
    path('newDetail/<int:id>/', views.newDetail, name='newDetail'),#新闻详情
]
