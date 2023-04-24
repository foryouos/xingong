from django.urls import path
from movieApp.views import movie,photo

app_name ='movieApp'

urlpatterns = [
    path('movie/',movie,name='movie'),
    path('photo/',photo,name='photo'),

]
