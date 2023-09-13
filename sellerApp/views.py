from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from sellerApp.models import *

@login_required
@csrf_exempt
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

