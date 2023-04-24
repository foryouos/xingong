from django.urls import path
from movieApp.views import movie,photo

app_name ='movieApp'
# 绑定子页面和名字
urlpatterns = [
    path('movie/',movie,name='movie'),
    path('photo/',photo,name='photo'),

]
