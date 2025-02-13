from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from books.utils import get_user_from_token
from .models import Book
from .serializers import BookSerializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated

@api_view(["GET"])
def get_books(request):
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(["POST"])
def create_book(request):
    """Create book only if user_type = 1 (Admin)"""
    user_data = get_user_from_token(request)

    if isinstance(user_data, Response):  
        return user_data  

    user_type = user_data.get("user_type")

    if user_type != 1:
        return Response({"detail": "You are not authorized to create books."}, status=status.HTTP_403_FORBIDDEN)

    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
