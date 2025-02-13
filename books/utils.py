from jose import jwt, JWTError
from django.conf import settings
from rest_framework.response import Response
from rest_framework import status

# SECRET_KEY = settings.SECRET_KEY  # Use the same key from FastAPI
SECRET_KEY = "vYwteHF2olSECLvniVb-XeBbgwXuhOT4fwhItyjORfo"
ALGORITHM = "HS256"  # Must match the algorithm used in FastAPI

def decode_jwt(token: str):
    """
    Decode JWT token and return the payload.
    """
    print(token, "token")
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        print(f"Decoded Payload: {payload}")  # Debugging output
        return payload
    except JWTError as e:
        print(f"JWT Decode Error: {e}")  # Debugging output
        return None  


def get_user_from_token(request):
    """
    Extracts token from request headers, decodes it, and returns the user data.
    """
    auth_header = request.headers.get("Authorization")
    
    if not auth_header:
        return Response({"detail": "Authorization header is missing"}, status=status.HTTP_401_UNAUTHORIZED)
    
    if not auth_header.startswith("Bearer "):
        return Response({"detail": "Invalid token format, must start with 'Bearer '"}, status=status.HTTP_401_UNAUTHORIZED)

    token = auth_header.split(" ")[1]  

    payload = decode_jwt(token)

    if not payload:
        return Response({"detail": "Invalid or expired token"}, status=status.HTTP_401_UNAUTHORIZED)

    return payload  

