from django.contrib import admin
from .models import Lunbo_main,Lunbo_video
# Register your models here.
# 修改管理员系统名称
admin.site.site_header = '新乡工程学院后台管理系统'
admin.site.site_title = '新乡工程学院后台管理系统'

#将model里面的函数添加到类当中  添加到注册到后台管理
class Lunbo_mainAdmin(admin.ModelAdmin):
    list_display = ['description','photo']
admin.site.register(Lunbo_main,Lunbo_mainAdmin)

class Lunbo_videoAdmin(admin.ModelAdmin):
    list_display = ['description','video']
admin.site.register(Lunbo_video,Lunbo_videoAdmin)