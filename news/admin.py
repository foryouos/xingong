from django.contrib import admin

from .models import News,newsImg

# Register your models here.
class NewsImgInline(admin.StackedInline):
    model = newsImg
    extra = 1 #默认显示条目数量
class NewsAdmin(admin.ModelAdmin):
    inlines = [NewsImgInline,]

admin.site.register(News,NewsAdmin)
