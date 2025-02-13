from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from books.utils import decode_jwt
from rest_framework.response import Response

class JWTAuthentication(BaseAuthentication):
    """
    Custom authentication class to validate JWT tokens.
    Extracts user data and adds it to the request object.
    """

    def authenticate(self, request):
        auth_header = request.headers.get("Authorization")

        if not auth_header or not auth_header.startswith("Bearer "):
            return None  # No authentication provided

        token = auth_header.split(" ")[1]  # Extract the token

        payload = decode_jwt(token)

        if not payload:
            raise AuthenticationFailed("Invalid or expired token")

        # Attach user data to request for later use
        request.user_data = payload
        return None  # DRF requires authentication classes to return a tuple (user, auth), but we don't use Django users
