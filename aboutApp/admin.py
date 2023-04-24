from django.contrib import admin

# Register your models here.
from .models import MyNew

# Register your models here.

class MyNewAdmin(admin.ModelAdmin):
    style_fields = {'description': 'ueditor'}

admin.site.register(MyNew, MyNewAdmin)
