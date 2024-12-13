from . import views
from django.urls import path

urlpatterns = [
    path('', views.get_all_books, name='get_all_books'),
    path('add', views.add_book, name='add_book'),
    path('id/<str:id>', views.get_book_by_id, name='get_book_by_id'),
    path('<str:id>/update', views.update_book, name='update_book'),
    path('<str:id>/delete', views.delete_book, name='delete_book'),
    path('isbn/<str:isbn>', views.get_book_by_isbn, name='get_book_by_isbn'),
    path('search', views.search_books, name='search_books'),
    path('filter', views.filter_books_by_genre, name='filter_books_by_genre'),
]