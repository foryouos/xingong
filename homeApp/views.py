from importlib import import_module
from django.shortcuts import render
from aboutApp.models import MyNew
from django.db.models import Q
from news.models import News,newsImg
from movieApp.models import School_Photo

# 动态渲染页面，引用轮播图，和轮播视频
from .models import Lunbo_main,Lunbo_video

# Create your views here.
def home(request):
    newList = MyNew.objects.all().filter(~Q(
        newType='招生信息')).order_by('-publishDate')
    postList = set()
    postNum = 0
    for s in newList:
        if s.photo:
            postList.add(s)
            postNum += 1
        if postNum == 3:  # 只截取最近的3个展报
            break
    # 新闻列表
    if (len(newList) > 7):
        newList = newList[0:7]    

    Lunbo_mains=Lunbo_main.objects.all()
    Lunbo_videos=Lunbo_video.objects.all()

    # 添加校园新闻
    newsList=News.objects.all()
    newsimgList=News.objects.all()
    # 显示新闻个数
    if (len(newsList) > 6):
        newsList = newsList[0:6]    


    school_photo = School_Photo.objects.all().order_by('-publishDate')
    return render(request,'home.html',{
        'active_menu':'home',
        'sub_menu':'home',
        'Lunbo_mains':Lunbo_mains,
        'Lunbo_videos':Lunbo_videos,
        'postList': postList,
        'newList': newList,
        'newsList':newsList,
        'newsimgList':newsimgList, 
        'school_photo':school_photo, 
     
    })