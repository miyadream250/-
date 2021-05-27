"""mysite1 URL Configuration

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
from django.urls import path, re_path, include

from mysite1 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("test/1", views.test_01),
    path("test/2", views.test_02),
    path("test/3", views.test_03),
    path("", views.index_view),
    re_path(r'^(?P<num1>\d{1,2})/(?P<mo>\w+)/(?P<num2>\d{1,2})$', views.calc_view),
    path("<int:num1>/<str:mo>/<int:num2>", views.calc_view),
    re_path(r'^birthday/(?P<mm>\d{1,2})/(?P<dd>\d{1,2})/(?P<yy>\d{4})$', views.birthday),
    re_path(r'^birthday/(?P<yy>\d{4})/(?P<mm>\d{1,2})/(?P<dd>\d{1,2})$', views.birthday),
    path("request_content", views.request_content),
    path("post_content", views.post_content),
    path("html_render", views.html_render),
    path("my_calc", views.my_calc),
    path("my_news", views.my_news, name="news"),
    path("my_music", views.my_music, name="my_music"),
    path("my_sport", views.my_sport, name="my_sport"),
    path("test_static", views.test_static),
    path("music/", include("music.urls")),
    path("sport/", include("sport.urls"))
]
