"""mysite2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from mysite2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index_templates', views.index_templates, name="index"),
    path('index', views.index_view),
    path("news/", include("news.urls")),
    path("music/", include("music.urls")),
    path("sport/", include("sport.urls")),
    path("bookstore/", include("bookstore.urls")),
    path("oto/", include("oto.urls")),
    path("set_cookie", views.set_cookie),
    path("get_cookie", views.get_cookie),
    path("get_session", views.get_session),
    path("set_session", views.set_session)

]
