from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect




def index_view(request):
    return HttpResponse("这是首页")


def index_templates(request):
    return render(request, "index.html")

