from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from sellerApp.models import *
from BookMyShow.permissionDecorator import *
from adminApp.models import *
from django.core import serializers
#from isodate import parse_duration



@login_required
@csrf_exempt
@user_type_required('seller')
def addTheater(request):
    try:
        data = json.loads(request.body)
        name = data.get('name')
        address = data.get('address')
        city = data.get('city')
        capacity = data.get('capacity')
        seller_id = data.get('seller_id') 
        addTheater = Theater(name = name, address = address, city = city, capacity = capacity, seller_id = seller_id)
        addTheater.save()
        return JsonResponse({"msg":"Theater added successfully"})
    except Exception as e:
        return JsonResponse({"msg":str(e)})

@login_required
@csrf_exempt
@user_type_required('seller')
def viewMovies(request):
    try:
       movies = list(Movie.objects.all().values())
       return JsonResponse(movies,safe=False)

        
       
    except Exception as e:
        return JsonResponse({"msg":str(e)})