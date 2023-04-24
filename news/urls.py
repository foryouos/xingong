from django.urls import path
from . import views

app_name ='newsApp'


urlpatterns = [
    path('news/<str:newsName>/', views.news, name='news'),#产品列表
    path('newsDetail/<int:id>/', views.newsDetail, name='newsDetail'),#产品详情
]
