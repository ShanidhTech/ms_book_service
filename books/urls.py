from django.urls import path
from .views import create_book, get_books  

urlpatterns = [
    path('books/', get_books, name='book-list'),   
    path('create/book/', create_book, name='create-book'),   
]
