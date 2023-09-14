from django.db import models
from authentication.models import *

class Admin(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'Admin'


class Movie(models.Model):

    name = models.CharField(50)
    time_duration = models.DurationField(null=False)
    release_date = models.DateField()
    description = models.TextField(max_length=200)
    admin = models.ForeignKey(Admin, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'Movie'
