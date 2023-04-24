from django.shortcuts import render
from movieApp.models import School_Photo
from django.core.paginator import Paginator
from news.models import News,newsImg
# Create your views here.
def movie(request):
    
    return render(
        request,'movie.html',
        {'active_menu':'movie',
        
        })
def photo(request):
    school_photo = School_Photo.objects.all().order_by('-publishDate')
    p = Paginator(school_photo, 6)
    if p.num_pages <= 1:
        pageData = ''
    else:
        page = int(request.GET.get('page', 1))
        school_photo = p.page(page)
        left = []
        right = []
        left_has_more = False
        right_has_more = False
        first = False
        last = False
        total_pages = p.num_pages
        page_range = p.page_range
        if page == 1:
            right = page_range[page:page + 2]
            print(total_pages)
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        elif page == total_pages:
            left = page_range[(page - 3) if (page - 3) > 0 else 0:page - 1]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
        else:
            left = page_range[(page - 3) if (page - 3) > 0 else 0:page - 1]
            right = page_range[page:page + 2]
            if left[0] > 2:
                left_has_more = True
            if left[0] > 1:
                first = True
            if right[-1] < total_pages - 1:
                right_has_more = True
            if right[-1] < total_pages:
                last = True
        pageData = {
            'left': left,
            'right': right,
            'left_has_more': left_has_more,
            'right_has_more': right_has_more,
            'first': first,
            'last': last,
            'total_pages': total_pages,
            'page': page,
        }


    return  render(
        request, 'photo.html', 
    {'active_menu': 'movie',
    'sub_menu': 'photo',
    'school_photo':school_photo,
    'pageData': pageData,

    })
# def photo(request):
#     AdList = Ad.objects.all().order_by('-publishDate')
    
#        # 添加校园新闻
#     newsList=News.objects.all()
#     newsimgList=News.objects.all()
#     # 显示新闻个数
#     if (len(newsList) > 6):
#         newsList = newsList[0:6]   
#     return render(
#         request, 'photo.html', {
#             'active_menu': 'contactus',
#             'sub_menu': 'recruit',
#             'AdList': AdList,
#             'newsList':newsList,
#             'newsimgList':newsimgList, 
           
#         })