from django.db import models
# 建立后台服务器需要的模型
# Create your models here.
#创建首页图片轮播后台数据库 k=Luobo_main
#
class Lunbo_main(models.Model):
    description=models.TextField(max_length=20,
                                 blank=True,
                                 null=True,
                                 verbose_name='轮播图片描述')
    photo = models.ImageField(upload_to='Lunbo_main/',
                              blank=True,
                              verbose_name='轮播图片')
    class Meta:
        verbose_name='轮播图片'
        verbose_name_plural='首页轮播图片'
# 定义视频轮播添加
class Lunbo_video(models.Model):
    description = models.TextField(max_length=20,
                                   blank=True,
                                   null=True,
                                   verbose_name='轮播视频描述')
    video =models.FileField(upload_to='lunbo_video/',
                            blank=True,
                            verbose_name='轮播视频')
    class Meta:
        verbose_name='轮播视频'
        verbose_name_plural='首页轮播视频'