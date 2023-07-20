
from rest_framework_simplejwt.authentication import JWTTokenUserAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken

class CookieJWTAuthentication(JWTTokenUserAuthentication):
    def get_token_from_request(self, request):
        # Retrieve the JWT token from the cookie
        token = request.COOKIES.get('jwt')
        print(token)
        if not token:
            print('token not found')
            return None
        print('token found')
        return token

    def get_validated_token(self, token):
        # Overriding this method to raise an exception if the token is invalid
        try:
            return super().get_validated_token(token)
        except InvalidToken:
            raise InvalidToken('Invalid token. Please log in again.')


