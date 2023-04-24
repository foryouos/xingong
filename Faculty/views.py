from django.shortcuts import render

# Create your views here.
def jidian(request):
    return render(request,'jidian.html',{'active_menu':'Faculty'})
def jingguan(request):
    return render(request,'jingguan.html',{'active_menu':'Faculty'})
def shengwu(request):
    return render(request,'shengwu.html',{'active_menu':'Faculty'})
def shipin(request):
    return render(request,'shipin.html',{'active_menu':'Faculty'})
def waiyu(request):
    return render(request,'waiyu.html',{'active_menu':'Faculty'})
def wenfa(request):
    return render(request,'wenfa.html',{'active_menu':'Faculty'})
def xinxi(request):
    return render(request,'xinxi.html',{'active_menu':'Faculty'})
def yishu(request):
    return render(request,'yishu.html',{'active_menu':'Faculty'})