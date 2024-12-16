from . import views
from django.urls import path

urlpatterns = [
    path('', views.get_all_bookshelves, name='get_all_bookshelves'),
    path('add', views.add_bookshelf, name='add_bookshelf'),
    path('<int:id>', views.get_bookshelf_by_id, name='get_bookshelf_by_id'),
    path('<int:id>/books', views.get_books_in_bookshelf, name='get_books_in_bookshelf'),
    path('<int:id>/update', views.update_bookshelf, name='update_bookshelf'),
    path('<int:id>/delete', views.delete_bookshelf, name='delete_bookshelf'),
    path('search', views.search_bookshelves, name='search_bookshelves'),
]