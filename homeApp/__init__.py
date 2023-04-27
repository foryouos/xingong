from os import path
from django.apps import AppConfig
# 后端首页显示 # 应用名称修改
VERBOSE_APP_NAME = '首页轮播'


def get_current_app_name(file):
    return path.dirname(file).replace('\\', '/').split('/')[-1]


class AppVerboseNameConfig(AppConfig):
    name = get_current_app_name(__file__)
    verbose_name = VERBOSE_APP_NAME


default_app_config = get_current_app_name(__file__) + '.__init__.AppVerboseNameConfig'
