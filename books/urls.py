from django.urls import path
from .views import create_book, get_books, update_book  

urlpatterns = [
    path('books/', get_books, name='book-list'),   
    path('create/book/', create_book, name='create-book'),   
    path("update/book/<int:book_id>/", update_book, name="update_book"),

]
