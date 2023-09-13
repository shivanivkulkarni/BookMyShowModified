
from django.contrib.auth.backends import ModelBackend
from authentication.models import *

class UserBackend(ModelBackend):
    def authenticate(self, request, username, password):
        try:
            print(username, password)
            user = CustomUser.objects.get(username=username)
            print(user)
            if user.check_password(password):
                return user
        except CustomUser.DoesNotExist:
            return None