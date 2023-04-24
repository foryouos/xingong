from django.apps import AppConfig


# 定义全局名字
class MovieConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'movieApp'
