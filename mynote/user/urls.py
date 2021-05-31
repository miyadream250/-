from django.contrib import admin
from django.urls import path

from user import views

urlpatterns = [
    path("register", views.reg_view),
    path("login", views.login_view)
]
