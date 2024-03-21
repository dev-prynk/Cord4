from rest_framework.authentication import BaseAuthentication
from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed

class Custom_Authentication(BaseAuthentication):
    def authenticate(self, request):
        username = request.GET.get('username')
        if username is None:
            return None
        
        try:
            user = User.objects.get(username=username)
            return (user, None) 
        except User.DoesNotExist:
            raise AuthenticationFailed("No user with the given username")