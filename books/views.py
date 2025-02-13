from rest_framework.response import Response
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework import status
from books.authentication import JWTAuthentication
from .models import Book
from .serializers import BookSerializer

@api_view(["GET"])
@authentication_classes([JWTAuthentication])
def get_books(request):
    """List all books"""
    books = Book.objects.all()
    serializer = BookSerializer(books, many=True)
    return Response(serializer.data)


@api_view(["POST"])
@authentication_classes([JWTAuthentication])
def create_book(request):
    """Create book only if user_type = 1 (Admin)"""

    user_type = request.user_data.get("user_type")  # Extract user_type

    if user_type != 1:
        return Response({"detail": "You are not authorized to create books."}, status=status.HTTP_403_FORBIDDEN)

    serializer = BookSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
