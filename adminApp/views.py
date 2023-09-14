from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login as auth_login
import json
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from BookMyShow.permissionDecorator import *
from adminApp.models import *

@csrf_exempt
@login_required
@user_type_required('admin')
def addMovie(request):
    try:
        data = json.loads(request.body)
        name = data.get('name')
        time_duration = data.get('time_duration')       
        release_date = data.get('release_date')
        description = data.get('description')
        admin_id = data.get('admin_id')
        movie = Movie(name = name,time_duration = time_duration, release_date = release_date, description = description, admin_id = admin_id)
        movie.save()
        return JsonResponse({"msg":"Movie added sucessfully"})
    except Exception as e:
        return JsonResponse({"msg":str(e)})






@csrf_exempt
def test(request):
    return JsonResponse({"msg":"test api"})
