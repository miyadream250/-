from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect


def index_view(request):
    return HttpResponse("这是首页")


def index_templates(request):
    return render(request, "index.html")


def set_cookie(request):
    res = HttpResponse("成功生成cookies")
    res.set_cookie("name", "gxn", max_age=500)
    return res


def get_cookie(request):
    res = request.COOKIES.get("name", "cookies时效")
    return HttpResponse("成功获取cookie %s" % res)
