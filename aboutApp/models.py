

# Create your models here.
from django.db import models
from DjangoUeditor.models import UEditorField
import django.utils.timezone as timezone

# Create your models here.

class MyNew(models.Model):
    NEWS_CHOICES = (
        ('招生信息', '招生信息'),
        ('招生政策', '招生政策'),
    )
    title = models.CharField(max_length=50, verbose_name=' 招生标题')
    description = UEditorField(u'内容',
                               default='',
                               width=1000,
                               height=300,
                               imagePath='zhaosheng/images/',
                               filePath='zhaosheng/files/')
    newType = models.CharField(choices=NEWS_CHOICES,
                               max_length=50,
                               verbose_name='招生类型')
    publishDate = models.DateTimeField(max_length=20,
                                       default=timezone.now,
                                       verbose_name='发布时间')
    photo = models.ImageField(upload_to='news/',
                              blank=True,
                              null=True,
                              verbose_name='展报')

    views = models.PositiveIntegerField('浏览量', default=0)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-publishDate']
        verbose_name = "招生信息"
        verbose_name_plural = verbose_name
