from django.db import models
# from DjangoUeditor.models import UEditorField
from django.utils import timezone
# Create your models here.

class News(models.Model):
    NEWS_CHOICES=(
        ('学校新闻','学校新闻'),
        ('通知公告','通知公告'),
        ('院部动态','院部动态'),
    )
    title=models.CharField(max_length=50,verbose_name='新闻名称')
    # description=UEditorField(u'内容',
    #                          default='',
    #                          width=1000,
    #                          height=300,
    #                          imagePath='news/images/',
    #                          filePath='news/files/',
    #                         )
    description = models.TextField(verbose_name='新闻描述')
    newsType=models.CharField(choices=NEWS_CHOICES,
                              max_length=50,
                              verbose_name='新闻类型')
    publishDate=models.DateTimeField(max_length=20,
                                     default=timezone.now,
                                     verbose_name='发布时间')
    views=models.PositiveIntegerField('浏览量',default=0)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name='学校新闻'
        verbose_name_plural='学校新闻'
        ordering = ['-publishDate']
class newsImg(models.Model):
    news=models.ForeignKey(News,
                           related_name='newsImgs',
                           verbose_name='新闻',
                           on_delete=models.CASCADE
                           )
    photo_title = models.CharField(max_length=10, verbose_name='图片描述',)
    photo=models.ImageField(upload_to='news/',
                            blank=True,
                            verbose_name='新闻图片')
    class Meta:
        verbose_name='新闻图片'
        verbose_name_plural='新闻图片'