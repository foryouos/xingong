"""djangoProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from homeApp.views import home
from django.urls.conf import include
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home,name='home'),
    path('movieApp/', include('movieApp.urls')),
    path('aboutApp/',include('aboutApp.urls')),
    path('Faculty/',include('Faculty.urls')),
    path('news/',include('news.urls')),
    path('ueditor/',include('DjangoUeditor.urls' )),  # 富文本应用
]

# 将动态资源配置添加到静态路由
from django.conf import settings
from django.conf.urls.static import static

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

