from django.shortcuts import render

# Create your views here.

from django.shortcuts import HttpResponse


def index_view(request):
    return render(request, "music/index.html")
    # return HttpResponse("我是music的index_view")
