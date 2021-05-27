from django.urls import path, re_path, include
from music import views

urlpatterns = [
    path("index", views.index_view)
]
