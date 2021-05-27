from django.shortcuts import render


# Create your views here.


def index_music(request):
    return render(request, "music/index.html")
