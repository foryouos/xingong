from django.db import models
from django.utils import timezone
# Create your models here.
# Create your models here.
class School_Photo(models.Model):
    description = models.TextField(max_length=500,
                                   blank=True,
                                   null=True)
    photo = models.ImageField(upload_to='School_Photo/',
                              blank=True)
    publishDate=models.DateTimeField(max_length=20,
                                     default=timezone.now,
                                     verbose_name='发布时间')
    def __str__(self):
        return self.description
    class Meta:
        verbose_name='学校风光'
        verbose_name_plural='学校风光'
        ordering = ['-publishDate']