# Generated by Django 4.0.4 on 2022-04-28 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lunbo_main',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(blank=True, max_length=20, null=True)),
                ('photo', models.ImageField(blank=True, upload_to='Lunbo_main/')),
            ],
        ),
    ]
