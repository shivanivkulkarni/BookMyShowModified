from django.db import models
from authentication.models import *

class Admin(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'Admin'
