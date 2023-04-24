# Generated by Django 4.0.4 on 2022-04-30 12:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0005_alter_newsimg_photo_title'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='news',
            options={'ordering': ['-publishDate'], 'verbose_name': '学校新闻', 'verbose_name_plural': '学校新闻'},
        ),
        migrations.AlterField(
            model_name='news',
            name='description',
            field=models.TextField(verbose_name='新闻描述'),
        ),
    ]
