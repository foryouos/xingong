from django.urls import path
from Faculty.views import jidian,jingguan,shipin,shengwu,waiyu,wenfa,xinxi,yishu
app_name ='Faculty'

urlpatterns = [
    path('jidian/',jidian,name='jidian'),
    path('jingguan/',jingguan,name='jingguan'),
    path('shipin/',shipin,name='shipin'),
    path('shengwu/',shengwu,name='shengwu'),
    path('waiyu/',waiyu,name='waiyu'),
    path('wenfa/',wenfa,name='wenfa'),
    path('xinxi/',xinxi,name='xinxi'),
    path('yishu/',yishu,name='yishu'),
]
