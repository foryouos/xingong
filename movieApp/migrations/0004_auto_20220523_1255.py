# Generated by Django 2.2.4 on 2022-05-23 04:55

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movieApp', '0003_school_photo'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='school_photo',
            options={'verbose_name': '学校风光', 'verbose_name_plural': '学校风光'},
        ),
        migrations.AddField(
            model_name='school_photo',
            name='publishDate',
            field=models.DateTimeField(default=django.utils.timezone.now, max_length=20, verbose_name='发布时间'),
        ),
    ]