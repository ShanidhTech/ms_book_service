from django.urls import path
from .views import *  

urlpatterns = [
    path('books/', get_books, name='book-list'),   
    path('create/book/', create_book, name='create-book'),   
    path("update/book/<int:book_id>/", update_book, name="update_book"),
    path("update/status/<int:book_id>/", change_book_status, name="change_book_status"),
]
