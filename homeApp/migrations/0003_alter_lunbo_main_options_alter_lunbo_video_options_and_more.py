# Generated by Django 4.0.4 on 2022-04-30 00:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeApp', '0002_lunbo_video'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lunbo_main',
            options={'verbose_name': '轮播图片', 'verbose_name_plural': '首页轮播图片'},
        ),
        migrations.AlterModelOptions(
            name='lunbo_video',
            options={'verbose_name': '轮播视频', 'verbose_name_plural': '首页轮播视频'},
        ),
        migrations.AlterField(
            model_name='lunbo_main',
            name='description',
            field=models.TextField(blank=True, max_length=20, null=True, verbose_name='轮播图片描述'),
        ),
        migrations.AlterField(
            model_name='lunbo_main',
            name='photo',
            field=models.ImageField(blank=True, upload_to='Lunbo_main/', verbose_name='轮播图片'),
        ),
        migrations.AlterField(
            model_name='lunbo_video',
            name='description',
            field=models.TextField(blank=True, max_length=20, null=True, verbose_name='轮播视频描述'),
        ),
        migrations.AlterField(
            model_name='lunbo_video',
            name='video',
            field=models.FileField(blank=True, upload_to='lunbo_video/', verbose_name='轮播视频'),
        ),
    ]
