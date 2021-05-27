from django.urls import path
from bookstore import views

urlpatterns = [
    path("all_book", views.all_book),
    path("update_book/<int:book_id>", views.update_book_view, name='update_info'),
    path("delete_book", views.delete_book)
]
