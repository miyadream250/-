from django.shortcuts import render


# Create your views here.
def index_news(request):
    return render(request, "news/index.html")
