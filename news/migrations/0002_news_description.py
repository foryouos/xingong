# Generated by Django 4.0.4 on 2022-04-30 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='description',
            field=models.TextField(default=1, verbose_name='新闻简略描述'),
            preserve_default=False,
        ),
    ]