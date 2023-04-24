# Generated by Django 2.2.4 on 2022-04-30 23:56

import DjangoUeditor.models
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MyNew',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name=' 招生标题')),
                ('description', DjangoUeditor.models.UEditorField(default='', verbose_name='内容')),
                ('newType', models.CharField(choices=[('招生信息', '招生信息'), ('招生政策', '招生政策')], max_length=50, verbose_name='招生类型')),
                ('publishDate', models.DateTimeField(default=django.utils.timezone.now, max_length=20, verbose_name='发布时间')),
                ('views', models.PositiveIntegerField(default=0, verbose_name='浏览量')),
            ],
            options={
                'verbose_name': '招生信息',
                'verbose_name_plural': '招生信息',
                'ordering': ['-publishDate'],
            },
        ),
    ]