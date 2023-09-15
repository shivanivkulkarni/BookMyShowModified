from django.db import models
from authentication.models import *

class Seller(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    name = models.CharField(max_length=50)

    class Meta:
        db_table = 'Seller'

class Theater(models.Model):
    name = models.CharField(max_length=100,unique=True)
    address=models.TextField()
    city=models.CharField(max_length=50)
    capacity=models.IntegerField()
    seller = models.ForeignKey(Seller, on_delete=models.CASCADE)

    class Meta:
        db_table = 'Theater'

