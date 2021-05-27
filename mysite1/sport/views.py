from django.shortcuts import render
from django.shortcuts import HttpResponse


# Create your views here.

def index_view(request):
    return render(request, "sport/index.html")
    # return HttpResponse("我是sport的index_views")
